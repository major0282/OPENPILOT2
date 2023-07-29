#!/usr/bin/env python3

import ast
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(message)s")

base_branches = [
  "master-ci",
  "release3"
]

def parse_cars():
  """
Parse the file with ast for a class named "CAR" and get a list of all the cars.
We are looking for the values in quotes.

Exerpt:

class CAR:
  # Hyundai
  ELANTRA = "HYUNDAI ELANTRA 2017"
  ELANTRA_2021 = "HYUNDAI ELANTRA 2021"
  ELANTRA_HEV_2021 = "HYUNDAI ELANTRA HYBRID 2021"
  HYUNDAI_GENESIS = "HYUNDAI GENESIS 2015-2016"
  IONIQ = "HYUNDAI IONIQ HYBRID 2017-2019"

`cars` should be an array of strings like this:

[
  "HYUNDAI ELANTRA 2017",
  "HYUNDAI ELANTRA 2021",
  "HYUNDAI ELANTRA HYBRID 2021",
  "HYUNDAI GENESIS 2015-2016",
  "HYUNDAI IONIQ HYBRID 2017-2019"
  ...
]

"""
  paths = [
  "comma_openpilot/selfdrive/car/hyundai/values.py"
  ]



  cars = []

  for path in paths:
    with open(path, "r") as f:
        tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "CAR":
                for c in node.body:
                    if isinstance(c, ast.Assign):
                        cars.append(c.value.s)


  # Log the cars
  logging.info("Found %d cars", len(cars))

  return cars

def prepare_op_repo():
  """
  Prepare the openpilot repo with master-ci and release3 branches
  """
  # Try to clone the repo to comma_openpilot.
  # If it fails, it means it already exists, so we can just pull
  # the latest changes.
  logging.info("Setting up openpilot repo. Ignore errors if it already exists.")

  os.system("git clone -b master-ci https://github.com/commaai/openpilot.git comma_openpilot")
  os.system("cd comma_openpilot && git fetch origin")
  os.system("cd comma_openpilot && git checkout release3 && git reset --hard origin/release3")
  os.system("cd comma_openpilot && git checkout master-ci && git reset --hard origin/master-ci")

  logging.info("Done setting up openpilot repo.")

def generate_branch(base, car):
  """
  Make a new branch for the car with a hardcoded fingerprint
  """
  branch_name = f"{base}-{car.replace(' ', '_').replace('&', 'AND').lower()}"
  logging.info("Generating branch %s", branch_name)
  # Delete branch if it already exists
  os.system(f"cd comma_openpilot && git branch -D {branch_name}")
  # Make branch off of base branch
  os.system(f"cd comma_openpilot && git checkout {base} && git checkout -b {branch_name}")
  # Make sure base branch is clean
  os.system(f"cd comma_openpilot && git reset --hard origin/{base}")
  # Append 'export FINGERPRINT="car name"' to the end of launch_env.sh
  os.system(f"echo 'export FINGERPRINT=\"{car}\"' >> comma_openpilot/launch_env.sh")
  # Commit the changes
  os.system(f"cd comma_openpilot && git add launch_env.sh && GIT_AUTHOR_DATE='Fri Jul 29 00:00:00 2023 -0700' GIT_COMMITTER_DATE='Fri Jul 29 00:00:00 2023 -0700' git commit -m 'Hardcode fingerprint for {car}'")
  return branch_name

def main():
  prepare_op_repo()
  cars = parse_cars()
  # Prepare OP repo
  # Limit to 1 car for now
  # cars = cars[:1]
  logging.info("Generating %d cars", len(cars))

  branch_names = []
  for base in base_branches:
    for car in cars:
      logging.info("Generating branch for %s", car)
      branch_name = generate_branch(base, car)
      branch_names.append(branch_name)

  logging.info("Done generating %d branches", len(branch_names))

  # Log the branch names
  logging.info("Branch names:")
  for branch_name in branch_names:
    logging.info(branch_name)
  # Run the command to push to origin all the branches
  logging.info("Pushing branches to origin")
  # Hardcoded
  os.system("cd comma_openpilot && git push --force https://github.com/hardcoded-fp/openpilot --all")



if __name__ == "__main__":
  main()

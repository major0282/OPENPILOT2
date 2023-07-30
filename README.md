# Hardcoded Fingerprint comma.ai openpilot Continuous Micro-Fork Generator

## How and Why to Use

openpilot queries the firmware of your vehicle upon start and configures itself to your vehicle accordingly with a list of pre-existing firmwares in the codebase. This process is called [Fingerprinting](https://github.com/commaai/openpilot/wiki/Fingerprinting). If you currently see an error of `Car Unrecognized: Dashcam Mode`, you should try to go through the [fingerprinting guide](https://github.com/commaai/openpilot/wiki/Fingerprinting). *Please make sure to follow the suggestion in the guide to try the `master-ci` branch first.*

If you are having trouble going through the fingerprinting guide, you can use this repository to install a version of openpilot on your vehicle with a hardcoded fingerprint so you can get things working ASAP. This method does not require knowledge of SSH, editing code, or modifying system files.

_Be aware that choosing and setting an erronous fingerprint can and usually will cause your vehicle and openpilot to behave unexpectedly_.

This repository is not to be considered a replacement for proper fingerprinting and should be used as an emergency, last, and temporary resort. As such, it does not apply cosmetic changes to the UI to disable warning messages such as "untested branch" as that is a genuine warning. Users of this should campaign and create an issue for the proper upstreaming of their fingerprints to the official openpilot repository. The commits of this repository are direct child commits of the official commits.

This GitHub repository periodically continuously generates openpilot branches off of openpilot's "deployment"-style and "unstable" `master-ci` branches with a hardcoded fingerprint identification of the vehicle for the purpose of installing the "unstable" `master-ci` flavor of openpilot on un-fingerprinted vehicles where there is currently fingerprinting trouble.

The branches here should be considered a temporary solution until the official openpilot repository is updated with the necessary fingerprints in the "unstable" `master-ci`. At which point, users should switch back to the official openpilot branches of "unstable" `master-ci` once their desired fingerprints are added to that branch.

A common feature suggestion for comma.ai's openpilot is to have a selectable vehicle selector in the settings if a vehicle is unrecognized. This is a temporary out-of-openpilot-codebase solution until such functionality is implemented and present.

You can see a list of fingerprint models, their corresponding branches, and their corresponding URLs for the [URL installer](https://github.com/commaai/openpilot/wiki/Forks#url-installers-at-installation-screen) here:

https://hardcoded-fp.github.io/openpilot/

## Example

So you got yourself a Hyundai Santa Fe Hybrid 2022 and you install the comma device. [It says it was supported on comma.ai's vehicles listing page](https://comma.ai/vehicles).

Once you do, you get `Car Unrecognized: Dashcam Mode` when you install `https://openpilot.comma.ai` on your comma device. That installer installed the "stable" `release3` branch of openpilot.

The next step is to [go through the fingerprinting guide and try the `master-ci` branch first as mentioned in the guide.](https://github.com/commaai/openpilot/wiki/Fingerprinting). If it works, you're done. If you want to get off the "unstable" `master-ci`, you may switch back to the "stable" `release3` branch when its new version is released by installing "Custom Software" `https://openpilot.comma.ai` again.

The fingerprint guide may be a bit daunting, so this repository is here as a last resort if you can't get through it.

If "unstable" `master-ci` doesn't work, stop here and consult the [comma.ai Discord](https://discord.comma.ai) channel for your car brand. In this case, the #hyundai-kia-genesis channel may recommend you force fingerprinting your vehicle as "HYUNDAI SANTA FE HYBRID 2022".

With this repository's [generated documentation](https://hardcoded-fp.github.io/openpilot/), you can find the corresponding branch with that hardcoded fingerprint. In this case, the corresponding branch is `master-ci-hyundai_santa_fe_hybrid_2022`. An installer URL to enter for Custom Software will be listed as well; in this case, it will be:

https://installer.comma.ai/hardcoded-fp/master-ci-hyundai_santa_fe_hybrid_2022

If all goes well, you'll run through the installation process and have "unstable" `master-ci` openpilot installed on your vehicle with a hardcoded fingerprint. When `master-ci` gets updated with the fingerprint for your vehicle, uninstall and switch back to the official `master-ci` branch. Please consult your brand's Discord channel for how to push your fingerprint upstream to the official openpilot repository and information on when it will be merged in.

## "Stable" `release3` Option

This GitHub repository also periodically continuously generates openpilot branches off of openpilot's "deployment"-style "stable" `release3` branches with a hardcoded fingerprint identification of the vehicle for the purpose of installing the respective "stable" `release3` flavors of openpilot on un-fingerprinted vehicles where there is currently a massive lag in the freshness of fingerprints in the "stable" `release3` compared to the "unstable" `master-ci` that has more current fingerprints but they want the possible increased "stable" `release3`'s stability.

Users who are forcing a fingerprint on "stable" `release3` to take advantage of the stability not present in `master-ci` should note that forced fingerprinting identities of vehicles into "stable" `release3` may turn it "unstable" and may cause unexpected behavior. Specific fingerprint data has historically been used to work around bugs in interactions with the vehicle of certain firmwares and such workarounds may not be present in the base "stable" `release3` codebase. If "stable" `release3` turns out to be "unstable", users should switch to the "unstable" `master-ci` branch and work with the community and developers to make it "stable" again in time for the next release of the "stable" `release3`.

## Design Questions

### Custom Forks?

This is generally not necessary for other forks as many of them have vehicle selectors. This is only useful for openpilot codebases without selectors such as comma.ai's official openpilot.

### Why not dynamically generate the installer and inject the fingerprint?

Injecting the fingerprint with the installer may produce non-pushed commits and/or non-commited code that can only be found on the device itself. By producing these branches periodically with GitHub, the commit on the device will have a commit in GitHub that can be referenced if help is sought.

## Welcome to [dwl-patches](https://codeberg.org/dwl/dwl-patches)!  
The dwl project is available at [https://codeberg.org/dwl/dwl](https://codeberg.org/dwl/dwl).  
This repository and the associated wiki is exclusively for dwl PATCHES.

## Patching
Since dwl follows [suckless](https://suckless.org/) philosophy it doesn't provide every feature under the sun. To broaden dwl's functionality, one needs to get familiar with the concept of patching. To get your feet wet, consult [the hacking page](https://suckless.org/hacking/) of the suckless website. Once you're ready to customize your build, proceed to the [dwl-patches wiki](https://codeberg.org/dwl/dwl-patches/wiki) which contains a categorized listing and a searchable sidebar index of all available patches.

**Note**: these external patches are user-submitted content, and the authors of dwl cannot monitor them. Please download and review a patch before using it!

## Creating Patches
1. Create a [Codeberg](https://codeberg.org) account and fork the [dwl](https://codeberg.org/dwl/dwl) repository.
2. Create a branch in your repository for the patch you are generating and maintaining. 
3. Make and test the modifications for your patch.

## Contributing Patches to this Wiki
1. If work has been done to the main branch at [dwl](https://codeberg.org/dwl/dwl) since you started work on your patch, REBASE YOUR PATCH!
2. In your local clone of your Codeberg dwl fork, add a remote for the main dwl repository:
    `git remote add codeberg-dwl https://codeberg.org/dwl/dwl`
3. In your local clone of your Codeberg dwl fork, create a .patch file
    `git --diff codeberg-dwl/main > PATCHNAME.patch`
4. Fork [https://codeberg.org/dwl/dwl-patches](https://codeberg.org/dwl/dwl-patches)
5. In your dwl-patches fork, add a directory called `PATCHNAME` and place the `PATCHNAME.patch` you created in step three into the `PATCHNAME` directory. You may also place screenshots in the `PATCHNAME` directory that you can later reference in your [dwl-patches wiki](https://codeberg.org/dwl/dwl-patches/wiki) entry.
6. Use the Codeberg web interface to send a pull request to [dwl-patches](https://codeberg.org/dwl/dwl-patches) (NOT to [dwl](https://codeberg.org/dwl/dwl))
7. WHEN YOUR PULL REQUEST IS APPROVED, your Codeberg user will also be granted commit access to [dwl-patches](https://codeberg.org/dwl/dwl-patches). When you make updates, replace your `PATCHNAME.patch` file directly. You no longer need to make pull requests. At this point, you will also have access to commit to the [dwl-patches wiki](https://codeberg.org/dwl/dwl-patches/wiki)
8. Add a wiki page using this template (add/remove sections as you like):
    ```markdown
    ### Description
    Insert a short summary of changes that your patch implements.

    ### Download
    - [yyyy-mm-dd](https://codeberg.org/dwl/dwl-patches/src/branch/main/PATCHNAME/PATCHNAME.patch)

    ### Authors and Patch Repositories
    - [YOURNAME](https://codeberg.org/YOURNAME/dwl/src/branch/PATCHNAME)
    ```
9. Use this template to add your patch to the [wiki](https://codeberg.org/dwl/dwl-patches/wiki)'s categorized list and sidebar index:
    ```markdown
    * [PATCHNAME](https://codeberg.org/dwl/dwl-patches/wiki/PATCHNAME)
    ```
10. Keep your `PATCHNAME.patch` file AND the associated wiki page updated appropriately.

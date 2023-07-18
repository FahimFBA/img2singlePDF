# img2singlePDF
A very short Python project to convert multiple image files to a single PDF file


## 🎥 Complete Video Tutorial (Click on the image)
[![How To Convert Multiple Images Into A PDF File Using Python || Python Project](https://img.youtube.com/vi/zBZhfzgahsk/maxresdefault.jpg)](https://www.youtube.com/watch?v=zBZhfzgahsk)

## 📦 Project Directory Structure

This is what project directory looks like without Git.

```
📦img2singlePDF
 ┣ 📜ImageContainingBook.pdf
 ┣ 📜jakub-neskora-A9tqu5iCFCQ-unsplash.jpg
 ┣ 📜raphael-renter-csae9W8JAsw-unsplash.jpg
 ┣ 📜README.md
 ┣ 📜sam-moghadam-khamseh-cU5TUyEaZXQ-unsplash.jpg
 ┣ 📜Script.py
 ┣ 📜sherry-christian-8Myh76_3M2U-unsplash.jpg
 ┗ 📜sunder-muthukumaran-fd6K_OFlnRA-unsplash.jpg

```

This is what my project looks like with the git and the necessary things for that.


<details>
<summary>This is a very long list! Expand it to display everything!</summary>
<br>

```
📦img2singlePDF
 ┣ 📂.git
 ┃ ┣ 📂hooks
 ┃ ┃ ┣ 📜applypatch-msg.sample
 ┃ ┃ ┣ 📜commit-msg.sample
 ┃ ┃ ┣ 📜fsmonitor-watchman.sample
 ┃ ┃ ┣ 📜post-update.sample
 ┃ ┃ ┣ 📜pre-applypatch.sample
 ┃ ┃ ┣ 📜pre-commit.sample
 ┃ ┃ ┣ 📜pre-merge-commit.sample
 ┃ ┃ ┣ 📜pre-push.sample
 ┃ ┃ ┣ 📜pre-rebase.sample
 ┃ ┃ ┣ 📜pre-receive.sample
 ┃ ┃ ┣ 📜prepare-commit-msg.sample
 ┃ ┃ ┣ 📜push-to-checkout.sample
 ┃ ┃ ┣ 📜sendemail-validate.sample
 ┃ ┃ ┗ 📜update.sample
 ┃ ┣ 📂info
 ┃ ┃ ┗ 📜exclude
 ┃ ┣ 📂logs
 ┃ ┃ ┣ 📂refs
 ┃ ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┃ ┗ 📂remotes
 ┃ ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┃ ┣ 📜HEAD
 ┃ ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📜HEAD
 ┃ ┣ 📂objects
 ┃ ┃ ┣ 📂0c
 ┃ ┃ ┃ ┗ 📜c08f36a8237d884055b437abdc7bca89f22df8
 ┃ ┃ ┣ 📂32
 ┃ ┃ ┃ ┗ 📜c5bb537b3090e578dfb85e718e67d020c32c76
 ┃ ┃ ┣ 📂3d
 ┃ ┃ ┃ ┗ 📜ded592bc5dd0578a155891368f664102883fca
 ┃ ┃ ┣ 📂45
 ┃ ┃ ┃ ┗ 📜e334d419d3876616469e28dca06f81aca486e7
 ┃ ┃ ┣ 📂4d
 ┃ ┃ ┃ ┗ 📜edc33ae7c102a040058caf2eadd3d477fd3e21
 ┃ ┃ ┣ 📂54
 ┃ ┃ ┃ ┣ 📜5f1fddb186d9780980728e966ffe9f54944c8c
 ┃ ┃ ┃ ┗ 📜ad4bb98b0a79bf810850ef26b93a7b9882a05f
 ┃ ┃ ┣ 📂59
 ┃ ┃ ┃ ┗ 📜8614d5c7e7add9218dd4553dff4f5f99f87f0c
 ┃ ┃ ┣ 📂5f
 ┃ ┃ ┃ ┗ 📜356de01c3c64b1021dde225503d639b0de2334
 ┃ ┃ ┣ 📂74
 ┃ ┃ ┃ ┗ 📜c39d53de4ce962e4ead056323d61b1c675ef18
 ┃ ┃ ┣ 📂7e
 ┃ ┃ ┃ ┗ 📜820efa4e5c2de055c33c6869b49e2785bb4ac3
 ┃ ┃ ┣ 📂83
 ┃ ┃ ┃ ┗ 📜4982131f2273474913da1365af6e2b5358f41b
 ┃ ┃ ┣ 📂90
 ┃ ┃ ┃ ┗ 📜04169f7f5de94569449f738637d612511b17d9
 ┃ ┃ ┣ 📂9a
 ┃ ┃ ┃ ┗ 📜d25664f1fe5729c9ea870cceef12c3c58b7231
 ┃ ┃ ┣ 📂b2
 ┃ ┃ ┃ ┗ 📜ccb86027fb7c17d7696b75d28a54f26b819957
 ┃ ┃ ┣ 📂b7
 ┃ ┃ ┃ ┗ 📜52e1abce94c356f4f3868aac7adaf474248d40
 ┃ ┃ ┣ 📂ba
 ┃ ┃ ┃ ┗ 📜349a61db8a1a1f079de33219556bf6b604b9a9
 ┃ ┃ ┣ 📂c2
 ┃ ┃ ┃ ┗ 📜c13133ebf295adaab5ba256b05087efe533a5d
 ┃ ┃ ┣ 📂ca
 ┃ ┃ ┃ ┗ 📜94f1cdc6a70faa9b7c5f3e954f96598cd3aed2
 ┃ ┃ ┣ 📂ce
 ┃ ┃ ┃ ┗ 📜23cc5cca425214374a8b8c84fb5eeecb4e0ba1
 ┃ ┃ ┣ 📂d3
 ┃ ┃ ┃ ┗ 📜59e6c3987f7d4888bf3207594694d89939da05
 ┃ ┃ ┣ 📂da
 ┃ ┃ ┃ ┗ 📜1926bd221081d98ac3d63f52fbe451649266a5
 ┃ ┃ ┣ 📂e4
 ┃ ┃ ┃ ┗ 📜51ae404388c90540cf32c6b80f2a15a4989dcd
 ┃ ┃ ┣ 📂fc
 ┃ ┃ ┃ ┗ 📜a21acf193c6a5a23f28f7faa2e97bff86bdf2d
 ┃ ┃ ┣ 📂info
 ┃ ┃ ┗ 📂pack
 ┃ ┃ ┃ ┣ 📜pack-906bdaa3745e4c955108eb06c6dbefac77f36ea6.idx
 ┃ ┃ ┃ ┣ 📜pack-906bdaa3745e4c955108eb06c6dbefac77f36ea6.pack
 ┃ ┃ ┃ ┗ 📜pack-906bdaa3745e4c955108eb06c6dbefac77f36ea6.rev
 ┃ ┣ 📂refs
 ┃ ┃ ┣ 📂heads
 ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┣ 📂remotes
 ┃ ┃ ┃ ┗ 📂origin
 ┃ ┃ ┃ ┃ ┣ 📜HEAD
 ┃ ┃ ┃ ┃ ┗ 📜main
 ┃ ┃ ┗ 📂tags
 ┃ ┣ 📜COMMIT_EDITMSG
 ┃ ┣ 📜config
 ┃ ┣ 📜description
 ┃ ┣ 📜FETCH_HEAD
 ┃ ┣ 📜HEAD
 ┃ ┣ 📜index
 ┃ ┣ 📜ORIG_HEAD
 ┃ ┗ 📜packed-refs
 ┣ 📂img
 ┃ ┗ 📜Preview.png
 ┣ 📂_includes
 ┃ ┗ 📜youtube.yml
 ┣ 📜.gitignore
 ┣ 📜ImageContainingBook.pdf
 ┣ 📜jakub-neskora-A9tqu5iCFCQ-unsplash.jpg
 ┣ 📜LICENSE
 ┣ 📜raphael-renter-csae9W8JAsw-unsplash.jpg
 ┣ 📜README.md
 ┣ 📜sam-moghadam-khamseh-cU5TUyEaZXQ-unsplash.jpg
 ┣ 📜Script.py
 ┣ 📜sherry-christian-8Myh76_3M2U-unsplash.jpg
 ┗ 📜sunder-muthukumaran-fd6K_OFlnRA-unsplash.jpg
 ```
 
</details>


## 📚 Used library

* img2pdf: https://pypi.org/project/img2pdf/


## 💻 Run the project

* Clone the repository `git clone https://github.com/FahimFBA/img2singlePDF.git`
* Go to the project directory `cd img2singlePDF`
* Install `img2pdf` library `pip install img2pdf`
* Change the file directory in the `Script.py` file
* Run the project `python Script.py`
* It will generate a pdf file named `ImageContainingBook.pdf` in the project directory


## ⭐ Stargazers

[![Stargazers repo roster for @FahimFBA/img2singlePDF](https://reporoster.com/stars/FahimFBA/img2singlePDF)](https://github.com/FahimFBA/img2singlePDF/stargazers)

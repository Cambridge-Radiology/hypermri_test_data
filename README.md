# Example MRI Data for Hypermri Docs

This repository contains example MRI datasets (e.g., `001_example_4`) for the `hypermri` documentation.

**Note:** It uses **Git LFS** for large files and a **pre-commit hook** to ensure MRI data is tracked correctly.

## 🚀 Setup

1.  **Install Prerequisites:**
    * [Git LFS](https://git-lfs.github.com/)
    * [pre-commit](https://pre-commit.com/) (e.g., `pip install pre-commit`)

2.  **Initialize LFS & Hooks:**
    ```bash
    git lfs install      # Set up Git LFS for your user account
    pre-commit install # Install hooks defined in .pre-commit-config.yaml
    ```

The pre-commit hook runs automatically on `git commit`. It will block the commit if binary files (like MRI images) are added without being tracked by Git LFS and will provide instructions to fix this.

## 🎯 Usage

1.  Add your example MRI data.
2.  Stage and commit files as usual (`git add .`, `git commit ...`).
3.  **If the pre-commit hook blocks the commit:**
    * It means binary files were added without being tracked by Git LFS.
    * Follow the printed instructions. You'll need to tell LFS to track the file(s). It's often best to track file *patterns*:
      ```bash
      # Example: Track all compressed NIfTI files in the repository
      git lfs track "*.nii.gz"

      # Or track the specific file reported by the hook 
      # git lfs track "path/to/offending/2dseq"
      ```
    * After running `git lfs track`, stage the updated `.gitattributes` file. The binary file(s) should typically already be staged from your initial `git add`.
      ```bash
      git add .gitattributes
      ```
    * Now, attempt the commit again:
      ```bash
      # Use the same commit message or amend the previous one
      git commit -m "Track large files with Git LFS"
      ```

## 🚀 Automatic Version Bumping

This repository uses **GitHub Actions** to automatically bump the version number of the project on every push to the `main` branch.

### How It Works:
- **Patch Bump**: Every time code is pushed to the `main` branch, the version will be bumped by **1 patch** version (e.g., `v0.0.1` → `v0.0.2`).
- **Minor Bump**: If a commit message contains `[bump:minor]`, the version will bump by **1 minor** version (e.g., `v0.1.0` → `v0.2.0`).
- **Major Bump**: If a commit message contains `[bump:major]`, the version will bump by **1 major** version (e.g., `v1.0.0` → `v2.0.0`).

### Example Commit Messages:
- **Default Patch Bump**:  
  `git commit -m "Update data [bump]"`  
  Version will bump from `v0.0.1` to `v0.0.2`.
  
- **Minor Bump**:  
  `git commit -m "Add new feature [bump:minor]"`  
  Version will bump from `v1.0.0` to `v1.1.0`.
  
- **Major Bump**:  
  `git commit -m "Breaking change [bump:major]"`  
  Version will bump from `v1.0.0` to `v2.0.0`.

### Version File:
The version is stored in the `VERSION` file located at the root of the repository. Each time a version bump occurs, this file will be updated with the new version number and pushed to GitHub along with the corresponding Git tag.
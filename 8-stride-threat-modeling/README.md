# STRIDE Threat Modeling

1. Update the git submodules

    ```zsh
    git submodule init
    git submodule update
    ```

2. Move into the `stride-gpt` subdir

    ```zsh
    cd stride-gpt
    ```

3. Install python requirements for `stride-gpt`

   ```zsh
   pip3 install -r requirements.txt
   ```

4. Run the `stride-gpt` app

   ```zsh
   streamlit run main.py
   ```

5. Describe an application and then generate the Threat Model, Attack Tree, and/or Mitigations.

    Three [app descriptions](app-descriptions.md) have been provided as examples.

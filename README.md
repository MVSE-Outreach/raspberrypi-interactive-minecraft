InteractiveMinecraft
====================

Scripts to make Minecraft: Pi Editon more interactive

If you have any problems, please contact me: graham@grahamlaming.co.uk

Downloading and running
-----------------------

1. Make sure you have git installed (`sudo apt-get install git-core`)
2. Download the source

    ```
    cd ~
    git clone https://github.com/glaming/InteractiveMinecraft.git
    ```

3. Start Minecraft: Pi Edition (assuming that it was extracted to ~/mcpi/)

    ```
    cd mcpi
    ./minecraft-pi &
    ```
    
4. Enter a Minecraft world
5. Run InteractiveMinecraft

    ```
    cd ~/InteractiveMinecraft
    python interactive.py
    ```

NOTE: The only useful commands implemented so far are 'copy' and 'quit'. When using the 'copy' command, follow the instructions provided inside the terminal.


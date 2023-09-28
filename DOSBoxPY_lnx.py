'''
Instructions for changing wizard:

Add, change, or remove categories by modifying the menuvalues list.
All you need to do is add a name, and you're set.
Add, change, or remove categories by modifying the submenuvalues list in either of the categories.
Each option should follow the same format as the existing options: "OptionName[option/values/with/no/limit/and spaces, as well as other symbols, can be added, too.]".
'''
import time
import sys
import os
import subprocess
#Actually get the fucking path to work. God help me.
dosbox_config_path = os.path.join('~', '.dosbox', 'dosbox-0.74-3.conf')
def restart_script():
    python_executable = sys.executable
    script_path = os.path.abspath(__file__)
    subprocess.call([python_executable, script_path])
def modify_settings(submenuvalues, start_line, menu_name):
    print(f"\nModifying {menu_name}\n")
    print("----------------------------------------------------------------------------")
    with open(dosbox_config_path, "r") as file:
        lines = file.readlines()

    for i, subitem in enumerate(submenuvalues, start=start_line):
        subitemname = subitem.split('[')[0].strip()
        subitemopt = subitem.split('[')[1].split(']')[0].replace('/', ', ')

        print(f"{i - start_line + 1}: {subitemname} [{subitemopt}]")

    for _ in range(19 - len(submenuvalues)):
        print("")

    choice = input("Enter the number of the setting you want to change: ")
    if choice == "back" or choice == "0":
        for _ in range(9000):
            print("")
        settings()

    value2 = input("Enter the new value: ")

    num1 = int(choice)
    if 1 <= num1 <= len(submenuvalues):
        result = num1 + start_line - 1
        if menu_name == "CPU":
            if num1 == len(submenuvalues):
                lines[result] = lines[result].split('=')[0] + "=" + value2 + "\n"
                lines[result + 1] = lines[result + 1].split('=')[0] + "=" + value2 + "\n"
            else:
                lines[result] = lines[result].split('=')[0] + "=" + value2 + "\n"
        else:
            lines[result] = lines[result].split('=')[0] + "=" + value2 + "\n"

        with open(dosbox_config_path, "w") as file:
            file.writelines(lines)
    else:
        lines[result] = lines[result].split('=')[0] + "=" + value2 + "\n"
    with open(dosbox_config_path, "w") as file:
        file.writelines(lines)
def settings():
    def edit_lines(lines, line_numbers, new_values):
        for i in range(len(line_numbers)):
            line_number = line_numbers[i]
            new_value = new_values[i]
            lines[line_number - 1] = lines[line_number - 1].split('=')[0] + "= " + new_value + "\n"
        return lines
    menuvalues = [
        "SDL", 
        "Emulated System", 
        "Rendering", 
        "CPU", 
        "Mixer", 
        "MIDI", 
        "SBlaster", 
        "Gravis Ultrasound Emulation", 
        "Speaker", 
        "Joystick", 
        "vSerial", 
        "General DOS Settings", 
        "Drives"
    ]

    print("")
    print("Modifying nothing yet.")
    print("")
    print("--------------------------------------------------------------------------------")

    num = 0
    for _ in range(len(menuvalues)):
        num += 1
        item = menuvalues[num - 1]
        print(f"{num}: {item}")

    for dummy in range(15 - len(menuvalues)):
        print("")

    print("re: Reset program. Will not reset settings..\nexit: Exit the program.\nIf you need help, contact me on GitHub. I'll be happy to help, and I'm always open to suggestions.")
    choice = input("Enter your choice: ")

    for dummy in range(9000):
        print("")
    if choice == 're':
        for dummy in range(9000):
            print("")
        settings()
    
    if choice == 'exit':
        print("Goodbye, and thank you for using this user-friendly interface, built by SwirlyStone5877.")
        time.sleep(1)
        sys.exit()
    if choice == '1':
        submenuvalues = [
            "Fullscreen[true/false]", 
            "Double Buffering in Fullscreen[true/false]", 
            "Resolution for Fullscreen[original/desktop]", 
            "Size to Scale Window to if Output Device Supports Hardware Scaling [original/desktop]", 
            "Video System for Output[surface/overlay/opengl/openglnb/ddraw]", 
            "Toggle Mouse Autolock[true/false]", 
            "Mouse Sensitivity[Any number/100 recommended]", 
            "Toggle Wait Before Closing Console if DOSBox has an Error[true/false]",
        ]
    
        modify_settings(submenuvalues, 25, menuvalues[int(choice) - 1]) # Start at line 26
    if choice == '2':
        submenuvalues = [
            "Machine to Emulate[hercules/cga/tandy/pcjr/ega/vgaonly/svga_s3/svga_et3000/svga_et4000/svga_paradise/vesa_nolfb/vesa_oldvbe]",
            "Directory Where Captures are Stored[Directory local to DOSBox installation.]",
            "Amount of Memory (GAME BREAKER AT TIMES)[Memory amount in MB.]",
        ]
        modify_settings(submenuvalues, 47, menuvalues[int(choice) - 1]) # Start at line 48
    if choice == '3':
        submenuvalues = [
            "Frameskip[Self-explanatory.]",
            "Aspect Correction[true/false]",
            "Scaler Used to Enhance Low Resolution Modes[none/normal2x/normal3x/advmame2x/advmame3x/advinterp2x/advinterp3x/hq2x/hq3x/2xsai/super2xsai/supereagle/tv2x/tv3x/rgb2x/rgb3x/scan2x/scan3x]",
        ]
        modify_settings(submenuvalues, 61, menuvalues[int(choice) - 1]) # Start at line 62
    if choice == '4':
        submenuvalues = [
            "CPU Core[auto/dynamic/normal/simple]",
            "CPU Type[auto/386/386_slow/486_slow/pentium_slow/386_prefetch]",
            "Cycles (Works in 3 ways. Auto just guesses. Fixed # will set a fixed amount. Max goes all out.) [auto/fixed #/max]",
            "Cycle Amount to Change with Keycombos. (CTRL-F11/CTRL-F12. Setting it lower than 100 will be a percentage.)[Any number.]", 
        ]
        modify_settings(submenuvalues, 85, menuvalues[int(choice) - 1]) # Start at line 86
    if choice == '5':
        submenuvalues = [
            "No Sound[true/false]",
            "Mixer Sample Rate (Setting any device's rate higher than this will probably lower their sound quality.)[44100/48000/32000/22050/16000/11025/8000/49716]",
            "Mixer Block Size (Larger blocks might help sound stuttering but sound will also be more lagged.)[1024/2048/4096/8192/512/256]",
            "Milliseconds of Data to Keep on Top of Blocksize.[Any number.]"
        ]
        modify_settings(submenuvalues, 98, menuvalues[int(choice) - 1]) # Start at line 99
    if choice == '6':
        submenuvalues = [
            "MPU-401 Type to Emulate[intelligent/uart/none]",
            "Device to receive MIDI data from MPU-401[default/win32/alsa/oss/coreaudio/coremidi/none]",
        ]
        modify_settings(submenuvalues, 113, menuvalues[int(choice) - 1]) # Start at line 114
    if choice == '7':
        submenuvalues = [
            "Soundblaster Type to Emulate (gb is GameBlaster.)[sb1/sb2/sbpro1/sbpro2/sb16/gb/none]", 
            "IO Address of Soundblaster[220/240/260/280/2a0/2c0/2e0/300]", 
            "IRQ Number of Soundblaster[7/5/3/9/10/11/12]", 
            "DMA Number of Soundblaster[1/5/0/3/6/7]", 
            "High DMA Number of Soundblaster[1/5/0/3/6/7]", 
            "Allow Soundblaster Mixer to Modify DOSBox Mixer[true/false]", 
            "OPL Emulation Type (CMS is not adlib compatible)[auto/cms/opl2/dualopl2/opl3/none]", 
            "OPL Emulation Provider[default/compat/fast]", 
            "OPL Music Emulation Sample Rate (Use 49716 for highest quality.)[44100/49716/48000/32000/22050/16000/11025/8000]", 
        ]
        modify_settings(submenuvalues, 136, menuvalues[int(choice) - 1]) # Start at line 137
    if choice == '8':
        submenuvalues = [
            "Enable GUS (Gravis UltraSound) Emulation[true/false]", 
            "GUS Sample Rate[44100/48000/32000/22050/16000/11025/8000/49716]", 
            "GUD IO Base[240/220/260/280/2a0/2c0/2e0/300]", 
            "IRQ Number of GUS[7/5/3/9/10/11/12]", 
            "DMA Number of Soundblaster[1/5/0/3/6/7]",  
            "Directory for GUS (In this directory there should be a MIDI directory that contains the patch files for GUS playback. Patch sets used with Timidity should work fine.)[[Directory local to DOSBox installation.]]",  
        ]
        modify_settings(submenuvalues, 161, menuvalues[int(choice) - 1]) # Start at line 162
    if choice == '9':
        submenuvalues = [
            "Enable PC Speaker Emulation[true/false]", 
            "Speaker Sample Rate[44100/48000/32000/22050/16000/11025/8000/49716]", 
            "Enable Tandy Sound System Emulation[true/false]", 
            "Tandy 3-Voice Generation Sample Rate[44100/48000/32000/22050/16000/11025/8000/49716]", 
            "Enable Disney Sound Source emulation[true/false]",  
        ]
        modify_settings(submenuvalues, 178, menuvalues[int(choice) - 1]) # Start at line 179
    if choice == '10':
        submenuvalues = [
            "Type of Joystick[auto (chooses emulation depending on real joystick)/2axis (supports two joysticks)/4axis (supports one joystick, first joystick used)/4axis_2 (supports one joystick, second joystick used)/fcs (Thrustmaster)/ch (CH Flightstick)/none]", 
            "Enable TimedIintervals for Axis (Experiment with this option if your joystick drifts.)[true/false]", 
            "Turbo[true/false]", 
            "Swap 3rd and 4th Axis[true/false]", 
            "Enable Button Wrapping at Number of Emulated Buttons[true/false]",  
        ]
        modify_settings(submenuvalues, 199, menuvalues[int(choice) - 1]) # Start at line 200
    if choice == '11':
        submenuvalues = [
            "vSerial 1[dummy/disabled/modem/nullmodem/directserial]", 
            "vSerial 2[dummy/disabled/modem/nullmodem/directserial]", 
            "vSerial 3[dummy/disabled/modem/nullmodem/directserial]",  
            "vSerial 4[dummy/disabled/modem/nullmodem/directserial]", 
        ]
        modify_settings(submenuvalues, 224, menuvalues[int(choice) - 1]) # Start at line 225
    if choice == '12':
        submenuvalues = [
            "XMS Support[true/false]", 
            "EMS Support[true/false]", 
            "UMB Support[true/false]"
        ]
        modify_settings(submenuvalues, 235, menuvalues[int(choice) - 1]) # Start at line 236
    if choice == '13':
        submenuvalues = [
            "Drive C",
            "Drive D",
        ]
        modify_settings(submenuvalues, 249, menuvalues[int(choice) - 1]) # Start at line 250
    if choice == 'back':
        restart_script()



    else:
        print("Invalid option! Unless you were editing a value, then this just pops up for no reason.")
        time.sleep(1)
        for dummy in range(9000):
            print("")
        settings()

print(f"\nMain Menu\n")
print("--------------------------------------------------------------------------------")
mainmenuvalues = [
    "Start DOSBox",
    "Settings",
    "About Menu Program"
]

num = 0
for _ in range(len(mainmenuvalues)):
    num += 1
    item = mainmenuvalues[num - 1]
    print(f"{num}: {item}")
for dummy in range(19 - len(mainmenuvalues)):
    print("")

choice = input("Enter your choice: ")
if choice == '1':
    os.system('dosbox -fullscreen -noconsole -userconf')
    restart_script()
if choice == '2':
    settings()
if choice == '3':
    print(f"\nAbout Menu Program\n")
    print("----------------------------------------------------------------------------")
    print(f"\n\n\n\n\n\n\n\n\nThank you for using the DOSBoxPy. If you have any questions, feel free to contact me at...\nMy Discord server at https://discord.gg/NKxxY6qeqC.\nMy GitHub at https://github.com/SwirlyStone5877\nMy email at swirlystone5877@gmail.com\n\nThis is a beta release and may not function properly.\nIf you see any bugs, report them.\nAs always, make backups.")
    input("\nPress Enter to continue...")
    restart_script()

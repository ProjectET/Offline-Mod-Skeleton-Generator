# The Dependencies
import numpy as np
import imageio
import os
import sys

# The Title, ASCI art and credits
os.system("title Mod Skeleton Generator")
print "  __  __           _    _____ _        _      _                 _____                           _             " + '\n' + " |  \\/  |         | |  / ____| |      | |    | |               / ____|                         | |            " + '\n' + " | \\  / | ___   __| | | (___ | | _____| | ___| |_ ___  _ __   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ " + '\n' + " | |\\/| |/ _ \\ / _` |  \\___ \\| |/ / _ \\ |/ _ \\ __/ _ \\| '_ \\  | | |_ |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|" + '\n' + " | |  | | (_) | (_| |  ____) |   <  __/ |  __/ || (_) | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   " + '\n' + " |_|  |_|\\___/ \\__,_| |_____/|_|\\_\\___|_|\\___|\\__\\___/|_| |_|  \\_____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   \n"
print "Created by ProjectET.\nOriginal mod skeleton generator by jopojelly."
print "--------------------------------------------------------------------------\n"

# Loop until one of the two commands are entered.
options = ["generate", "quit"]
while True:
    In = raw_input("To begin generating files type 'generate', to close the generator type 'quit': ")
    if In in options: 
        break
    elif In == "":
        print "No command entered. Enter 'generate' or 'quit'.\n"
    else:
        print "Invalid command. Enter 'generate' or 'quit'.\n"

# File Generation
if In == "generate":
    # Clears the console and reprints the menu
    clear = lambda: os.system('cls')
    clear()
    print "  __  __           _    _____ _        _      _                 _____                           _             " + '\n' + " |  \\/  |         | |  / ____| |      | |    | |               / ____|                         | |            " + '\n' + " | \\  / | ___   __| | | (___ | | _____| | ___| |_ ___  _ __   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ " + '\n' + " | |\\/| |/ _ \\ / _` |  \\___ \\| |/ / _ \\ |/ _ \\ __/ _ \\| '_ \\  | | |_ |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|" + '\n' + " | |  | | (_) | (_| |  ____) |   <  __/ |  __/ || (_) | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   " + '\n' + " |_|  |_|\\___/ \\__,_| |_____/|_|\\_\\___|_|\\___|\\__\\___/|_| |_|  \\_____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   \n"
    print "Created by ProjectET.\nOriginal mod skeleton generator by jopojelly."
    print "--------------------------------------------------------------------------\n"
    print "For Mod Name and 1st Item's Name, don't use apostrophes or other special characters.\n"
    
    # Assigning values to variables
    z = 0
    x = 0
    c = 0
    v = 0
    erz = ""
    erx = ""
    erc = ""
    erv = ""
    Ite = "Items"
    
    # Error checker, if input is empty it raises an error is not then assigns a variable to 1.
    try:
        Mn = raw_input("Enter Mod name (No spaces or special characters): ")
        if not Mn:
            raise ValueError
        else:
            z = 1
    except ValueError:
        erz = "Mod name"
    
    try:
        Md = raw_input("Enter Mod display name: ")
        if not Md:
            raise ValueError
        else:
            x = 1
    except ValueError:
        erx = "Mod display name"

    try:
        It = raw_input("Enter 1st Item's name (No spaces or special characters): ")
        if not It:
            raise ValueError
        else:
            c = 1
    except ValueError:
        erc = "1st Item's name"
    
    try:
        MA = raw_input("Enter your username: ")
        if not MA:
            raise ValueError
        else:
            v = 1
    except ValueError:
        erv = "Username"

    # adds all the error checker variables together, if it adds to 4 then it continues generating files, if not then raises an error
    b = z + x + c + v
    if b == 4:
        # Generates the build file
        os.makedirs(os.path.join(Mn, Ite))
        nl = '\n'
        buildtxt = os.path.join(Mn, "build.txt")
        build = open(buildtxt, "w")
        build.write("author = " + MA + nl)
        build.write("version = 0.1" + nl)
        build.write("displayName = " + Md)
        
        # Generates the description file        
        desctxt = os.path.join(Mn, "description.txt")
        desc = open(desctxt, "w")
        desc.write(Md + " is a pretty cool mod, it does...this. Modify this file with a description of your mod.")

        # Generates the item code which is the example sword.
        Itemcs = os.path.join(Mn, Ite, It + '.cs')
        Itcs = open(Itemcs, "w")
        Itcs.write("using Terraria.ID;" + nl + "using Terraria.Modloader;" + nl + nl + "namespace " + Mn + '.Items' + nl + "{" + nl + "  public class " + It + ' : ModItem' + nl)
        Itcs.write("	{" + nl + "		public overide void SetStaticDefaults()" + nl + "		{" + nl + '			DisplayName.SetDefault("' + It + '");' + nl)
        Itcs.write('			Tooltip.SetDefault("This is a modded sword.");' + nl + '		}' + nl + '		public override void SetDefaults()' + nl + '		{' + nl)
        Itcs.write('			item.damage = 50;' + nl + '			item.melee = true;' + nl + '			item.width = 40;' + nl + '			item.height = 40;' + nl)
        Itcs.write('			item.useTime = 20;' + nl + '			item.useAnimation = 20;' + nl + '			item.useStyle = 1;' + nl + '			item.knockback = 6;' + nl)
        Itcs.write('			item.value = 10000;' + nl + '			item.rare = 2;' + nl + '			item.UseSound = SoundID.Item1;' + nl + '			item.autoReuse = true;' + nl)
        Itcs.write('		}' + nl + nl + '		public override void AddRecipes()' + nl + '		{' + nl + '			ModRecipe recipe = new ModRecipe(mod);' + nl)
        Itcs.write('			recipe.AddIngredient(ItemID.DirtBlock, 10);' + nl + '			recipe.AddTile(TileID.WorkBenches);' + nl + '			recipe.SetResult(this);' + nl)
        Itcs.write('			recipe.AddRecipe();' + nl + '		}' + nl + '	}' + nl + '}')

        # Generates the 40x40 image, the 'data[y,x] = <var>' are the pixel values. This is the code that significantly increased file size.
        data = np.zeros( (40,40,4), dtype=np.uint8 )
        
        # These <var> assigns the colour (color if you are American) values.
        tra = [0,0,0,0]
        bla = [26,26,26,255]
        dgr = [102,102,102,255]
        lgr = [178,178,178,255]
        whi = [204,204,204,255]

        data[0,0] = tra; data[1,0] = tra; data[2,0] = tra; data[3,0] = tra; data[4,0] = tra; data[5,0] = tra; data[6,0] = tra; data[7,0] = tra; data[8,0] = tra; data[9,0] = tra; data[10,0] = tra; data[11,0] = tra; data[12,0] = tra; data[13,0] = tra; data[14,0] = tra; data[15,0] = tra; data[16,0] = tra; data[17,0] = tra; data[18,0] = tra; data[19,0] = tra; data[20,0] = tra; data[21,0] = tra; data[22,0] = tra; data[23,0] = tra; data[24,0] = tra; data[25,0] = tra; data[26,0] = tra; data[27,0] = tra; data[28,0] = tra; data[29,0] = tra; data[30,0] = tra; data[31,0] = tra; data[32,0] = tra; data[33,0] = tra; data[34,0] = tra; data[35,0] = tra; data[36,0] = bla; data[37,0] = bla; data[38,0] = bla; data[39,0] = bla
        data[0,1] = tra; data[1,1] = tra; data[2,1] = tra; data[3,1] = tra; data[4,1] = tra; data[5,1] = tra; data[6,1] = tra; data[7,1] = tra; data[8,1] = tra; data[9,1] = tra; data[10,1] = tra; data[11,1] = tra; data[12,1] = tra; data[13,1] = tra; data[14,1] = tra; data[15,1] = tra; data[16,1] = tra; data[17,1] = tra; data[18,1] = tra; data[19,1] = tra; data[20,1] = tra; data[21,1] = tra; data[22,1] = tra; data[23,1] = tra; data[24,1] = tra; data[25,1] = tra; data[26,1] = tra; data[27,1] = tra; data[28,1] = tra; data[29,1] = tra; data[30,1] = tra; data[31,1] = tra; data[32,1] = tra; data[33,1] = tra; data[34,1] = tra; data[35,1] = tra; data[36,1] = bla; data[37,1] = bla; data[38,1] = bla; data[39,1] = bla
        data[0,2] = tra; data[1,2] = tra; data[2,2] = tra; data[3,2] = tra; data[4,2] = tra; data[5,2] = tra; data[6,2] = tra; data[7,2] = tra; data[8,2] = tra; data[9,2] = tra; data[10,2] = tra; data[11,2] = tra; data[12,2] = tra; data[13,2] = tra; data[14,2] = tra; data[15,2] = tra; data[16,2] = tra; data[17,2] = tra; data[18,2] = tra; data[19,2] = tra; data[20,2] = tra; data[21,2] = tra; data[22,2] = tra; data[23,2] = tra; data[24,2] = bla; data[25,2] = bla; data[26,2] = bla; data[27,2] = bla; data[28,2] = tra; data[29,2] = tra; data[30,2] = tra; data[31,2] = tra; data[32,2] = tra; data[33,2] = tra; data[34,2] = bla; data[35,2] = bla; data[36,2] = dgr; data[37,2] = dgr; data[38,2] = bla; data[39,2] = bla
        data[0,3] = tra; data[1,3] = tra; data[2,3] = tra; data[3,3] = tra; data[4,3] = tra; data[5,3] = tra; data[6,3] = tra; data[7,3] = tra; data[8,3] = tra; data[9,3] = tra; data[10,3] = tra; data[11,3] = tra; data[12,3] = tra; data[13,3] = tra; data[14,3] = tra; data[15,3] = tra; data[16,3] = tra; data[17,3] = tra; data[18,3] = tra; data[19,3] = tra; data[20,3] = tra; data[21,3] = tra; data[22,3] = tra; data[23,3] = tra; data[24,3] = bla; data[25,3] = bla; data[26,3] = bla; data[27,3] = bla; data[28,3] = tra; data[29,3] = tra; data[30,3] = tra; data[31,3] = tra; data[32,3] = tra; data[33,3] = tra; data[34,3] = bla; data[35,3] = bla; data[36,3] = dgr; data[37,3] = dgr; data[38,3] = bla; data[39,3] = bla
        data[0,4] = tra; data[1,4] = tra; data[2,4] = tra; data[3,4] = tra; data[4,4] = tra; data[5,4] = tra; data[6,4] = tra; data[7,4] = tra; data[8,4] = tra; data[9,4] = tra; data[10,4] = tra; data[11,4] = tra; data[12,4] = tra; data[13,4] = tra; data[14,4] = tra; data[15,4] = tra; data[16,4] = tra; data[17,4] = tra; data[18,4] = tra; data[19,4] = tra; data[20,4] = tra; data[21,4] = tra; data[22,4] = tra; data[23,4] = tra; data[24,4] = bla; data[25,4] = bla; data[26,4] = dgr; data[27,4] = dgr; data[28,4] = bla; data[29,4] = bla; data[30,4] = tra; data[31,4] = tra; data[32,4] = bla; data[33,4] = bla; data[34,4] = dgr; data[35,4] = dgr; data[36,4] = bla; data[37,4] = bla; data[38,4] = tra; data[39,4] = tra
        data[0,5] = tra; data[1,5] = tra; data[2,5] = tra; data[3,5] = tra; data[4,5] = tra; data[5,5] = tra; data[6,5] = tra; data[7,5] = tra; data[8,5] = tra; data[9,5] = tra; data[10,5] = tra; data[11,5] = tra; data[12,5] = tra; data[13,5] = tra; data[14,5] = tra; data[15,5] = tra; data[16,5] = tra; data[17,5] = tra; data[18,5] = tra; data[19,5] = tra; data[20,5] = tra; data[21,5] = tra; data[22,5] = tra; data[23,5] = tra; data[24,5] = bla; data[25,5] = bla; data[26,5] = dgr; data[27,5] = dgr; data[28,5] = bla; data[29,5] = bla; data[30,5] = tra; data[31,5] = tra; data[32,5] = bla; data[33,5] = bla; data[34,5] = dgr; data[35,5] = dgr; data[36,5] = bla; data[37,5] = bla; data[38,5] = tra; data[39,5] = tra
        data[0,6] = tra; data[1,6] = tra; data[2,6] = tra; data[3,6] = tra; data[4,6] = tra; data[5,6] = tra; data[6,6] = tra; data[7,6] = tra; data[8,6] = tra; data[9,6] = tra; data[10,6] = tra; data[11,6] = tra; data[12,6] = tra; data[13,6] = tra; data[14,6] = tra; data[15,6] = tra; data[16,6] = tra; data[17,6] = tra; data[18,6] = tra; data[19,6] = tra; data[20,6] = tra; data[21,6] = tra; data[22,6] = tra; data[23,6] = tra; data[24,6] = tra; data[25,6] = tra; data[26,6] = bla; data[27,6] = bla; data[28,6] = dgr; data[29,6] = dgr; data[30,6] = bla; data[31,6] = bla; data[32,6] = dgr; data[33,6] = dgr; data[34,6] = bla; data[35,6] = bla; data[36,6] = tra; data[37,6] = tra; data[38,6] = tra; data[39,6] = tra
        data[0,7] = tra; data[1,7] = tra; data[2,7] = tra; data[3,7] = tra; data[4,7] = tra; data[5,7] = tra; data[6,7] = tra; data[7,7] = tra; data[8,7] = tra; data[9,7] = tra; data[10,7] = tra; data[11,7] = tra; data[12,7] = tra; data[13,7] = tra; data[14,7] = tra; data[15,7] = tra; data[16,7] = tra; data[17,7] = tra; data[18,7] = tra; data[19,7] = tra; data[20,7] = tra; data[21,7] = tra; data[22,7] = tra; data[23,7] = tra; data[24,7] = tra; data[25,7] = tra; data[26,7] = bla; data[27,7] = bla; data[28,7] = dgr; data[29,7] = dgr; data[30,7] = bla; data[31,7] = bla; data[32,7] = dgr; data[33,7] = dgr; data[34,7] = bla; data[35,7] = bla; data[36,7] = tra; data[37,7] = tra; data[38,7] = tra; data[39,7] = tra
        data[0,8] = tra; data[1,8] = tra; data[2,8] = tra; data[3,8] = tra; data[4,8] = tra; data[5,8] = tra; data[6,8] = tra; data[7,8] = tra; data[8,8] = tra; data[9,8] = tra; data[10,8] = tra; data[11,8] = tra; data[12,8] = tra; data[13,8] = tra; data[14,8] = tra; data[15,8] = tra; data[16,8] = tra; data[17,8] = tra; data[18,8] = tra; data[19,8] = tra; data[20,8] = tra; data[21,8] = tra; data[22,8] = tra; data[23,8] = tra; data[24,8] = tra; data[25,8] = tra; data[26,8] = bla; data[27,8] = bla; data[28,8] = bla; data[29,8] = bla; data[30,8] = dgr; data[31,8] = dgr; data[32,8] = bla; data[33,8] = bla; data[34,8] = tra; data[35,8] = tra; data[36,8] = tra; data[37,8] = tra; data[38,8] = tra; data[39,8] = tra
        data[0,9] = tra; data[1,9] = tra; data[2,9] = tra; data[3,9] = tra; data[4,9] = tra; data[5,9] = tra; data[6,9] = tra; data[7,9] = tra; data[8,9] = tra; data[9,9] = tra; data[10,9] = tra; data[11,9] = tra; data[12,9] = tra; data[13,9] = tra; data[14,9] = tra; data[15,9] = tra; data[16,9] = tra; data[17,9] = tra; data[18,9] = tra; data[19,9] = tra; data[20,9] = tra; data[21,9] = tra; data[22,9] = tra; data[23,9] = tra; data[24,9] = tra; data[25,9] = tra; data[26,9] = bla; data[27,9] = bla; data[28,9] = bla; data[29,9] = bla; data[30,9] = dgr; data[31,9] = dgr; data[32,9] = bla; data[33,9] = bla; data[34,9] = tra; data[35,9] = tra; data[36,9] = tra; data[37,9] = tra; data[38,9] = tra; data[39,9] = tra
        data[0,10] = tra; data[1,10] = tra; data[2,10] = tra; data[3,10] = tra; data[4,10] = tra; data[5,10] = tra; data[6,10] = tra; data[7,10] = tra; data[8,10] = tra; data[9,10] = tra; data[10,10] = tra; data[11,10] = tra; data[12,10] = tra; data[13,10] = tra; data[14,10] = tra; data[15,10] = tra; data[16,10] = tra; data[17,10] = tra; data[18,10] = tra; data[19,10] = tra; data[20,10] = tra; data[21,10] = tra; data[22,10] = tra; data[23,10] = tra; data[24,10] = bla; data[25,10] = bla; data[26,10] = whi; data[27,10] = whi; data[28,10] = lgr; data[29,10] = lgr; data[30,10] = bla; data[31,10] = bla; data[32,10] = dgr; data[33,10] = dgr; data[34,10] = bla; data[35,10] = bla; data[36,10] = tra; data[37,10] = tra; data[38,10] = tra; data[39,10] = tra
        data[0,11] = tra; data[1,11] = tra; data[2,11] = tra; data[3,11] = tra; data[4,11] = tra; data[5,11] = tra; data[6,11] = tra; data[7,11] = tra; data[8,11] = tra; data[9,11] = tra; data[10,11] = tra; data[11,11] = tra; data[12,11] = tra; data[13,11] = tra; data[14,11] = tra; data[15,11] = tra; data[16,11] = tra; data[17,11] = tra; data[18,11] = tra; data[19,11] = tra; data[20,11] = tra; data[21,11] = tra; data[22,11] = tra; data[23,11] = tra; data[24,11] = bla; data[25,11] = bla; data[26,11] = whi; data[27,11] = whi; data[28,11] = lgr; data[29,11] = lgr; data[30,11] = bla; data[31,11] = bla; data[32,11] = dgr; data[33,11] = dgr; data[34,11] = bla; data[35,11] = bla; data[36,11] = tra; data[37,11] = tra; data[38,11] = tra; data[39,11] = tra
        data[0,12] = tra; data[1,12] = tra; data[2,12] = tra; data[3,12] = tra; data[4,12] = tra; data[5,12] = tra; data[6,12] = tra; data[7,12] = tra; data[8,12] = tra; data[9,12] = tra; data[10,12] = tra; data[11,12] = tra; data[12,12] = tra; data[13,12] = tra; data[14,12] = tra; data[15,12] = tra; data[16,12] = tra; data[17,12] = tra; data[18,12] = tra; data[19,12] = tra; data[20,12] = tra; data[21,12] = tra; data[22,12] = bla; data[23,12] = bla; data[24,12] = whi; data[25,12] = whi; data[26,12] = lgr; data[27,12] = lgr; data[28,12] = whi; data[29,12] = whi; data[30,12] = bla; data[31,12] = bla; data[32,12] = bla; data[33,12] = bla; data[34,12] = dgr; data[35,12] = dgr; data[36,12] = bla; data[37,12] = bla; data[38,12] = tra; data[39,12] = tra
        data[0,13] = tra; data[1,13] = tra; data[2,13] = tra; data[3,13] = tra; data[4,13] = tra; data[5,13] = tra; data[6,13] = tra; data[7,13] = tra; data[8,13] = tra; data[9,13] = tra; data[10,13] = tra; data[11,13] = tra; data[12,13] = tra; data[13,13] = tra; data[14,13] = tra; data[15,13] = tra; data[16,13] = tra; data[17,13] = tra; data[18,13] = tra; data[19,13] = tra; data[20,13] = tra; data[21,13] = tra; data[22,13] = bla; data[23,13] = bla; data[24,13] = whi; data[25,13] = whi; data[26,13] = lgr; data[27,13] = lgr; data[28,13] = whi; data[29,13] = whi; data[30,13] = bla; data[31,13] = bla; data[32,13] = bla; data[33,13] = bla; data[34,13] = dgr; data[35,13] = dgr; data[36,13] = bla; data[37,13] = bla; data[38,13] = tra; data[39,13] = tra
        data[0,14] = tra; data[1,14] = tra; data[2,14] = tra; data[3,14] = tra; data[4,14] = tra; data[5,14] = tra; data[6,14] = tra; data[7,14] = tra; data[8,14] = tra; data[9,14] = tra; data[10,14] = tra; data[11,14] = tra; data[12,14] = tra; data[13,14] = tra; data[14,14] = tra; data[15,14] = tra; data[16,14] = tra; data[17,14] = tra; data[18,14] = tra; data[19,14] = tra; data[20,14] = bla; data[21,14] = bla; data[22,14] = whi; data[23,14] = whi; data[24,14] = lgr; data[25,14] = lgr; data[26,14] = whi; data[27,14] = whi; data[28,14] = bla; data[29,14] = bla; data[30,14] = tra; data[31,14] = tra; data[32,14] = tra; data[33,14] = tra; data[34,14] = bla; data[35,14] = bla; data[36,14] = bla; data[37,14] = bla; data[38,14] = tra; data[39,14] = tra
        data[0,15] = tra; data[1,15] = tra; data[2,15] = tra; data[3,15] = tra; data[4,15] = tra; data[5,15] = tra; data[6,15] = tra; data[7,15] = tra; data[8,15] = tra; data[9,15] = tra; data[10,15] = tra; data[11,15] = tra; data[12,15] = tra; data[13,15] = tra; data[14,15] = tra; data[15,15] = tra; data[16,15] = tra; data[17,15] = tra; data[18,15] = tra; data[19,15] = tra; data[20,15] = bla; data[21,15] = bla; data[22,15] = whi; data[23,15] = whi; data[24,15] = lgr; data[25,15] = lgr; data[26,15] = whi; data[27,15] = whi; data[28,15] = bla; data[29,15] = bla; data[30,15] = tra; data[31,15] = tra; data[32,15] = tra; data[33,15] = tra; data[34,15] = bla; data[35,15] = bla; data[36,15] = bla; data[37,15] = bla; data[38,15] = tra; data[39,15] = tra
        data[0,16] = tra; data[1,16] = tra; data[2,16] = tra; data[3,16] = tra; data[4,16] = tra; data[5,16] = tra; data[6,16] = tra; data[7,16] = tra; data[8,16] = tra; data[9,16] = tra; data[10,16] = tra; data[11,16] = tra; data[12,16] = tra; data[13,16] = tra; data[14,16] = tra; data[15,16] = tra; data[16,16] = tra; data[17,16] = tra; data[18,16] = bla; data[19,16] = bla; data[20,16] = whi; data[21,16] = whi; data[22,16] = lgr; data[23,16] = lgr; data[24,16] = whi; data[25,16] = whi; data[26,16] = bla; data[27,16] = bla; data[28,16] = tra; data[29,16] = tra; data[30,16] = tra; data[31,16] = tra; data[32,16] = tra; data[33,16] = tra; data[34,16] = tra; data[35,16] = tra; data[36,16] = tra; data[37,16] = tra; data[38,16] = tra; data[39,16] = tra
        data[0,17] = tra; data[1,17] = tra; data[2,17] = tra; data[3,17] = tra; data[4,17] = tra; data[5,17] = tra; data[6,17] = tra; data[7,17] = tra; data[8,17] = tra; data[9,17] = tra; data[10,17] = tra; data[11,17] = tra; data[12,17] = tra; data[13,17] = tra; data[14,17] = tra; data[15,17] = tra; data[16,17] = tra; data[17,17] = tra; data[18,17] = bla; data[19,17] = bla; data[20,17] = whi; data[21,17] = whi; data[22,17] = lgr; data[23,17] = lgr; data[24,17] = whi; data[25,17] = whi; data[26,17] = bla; data[27,17] = bla; data[28,17] = tra; data[29,17] = tra; data[30,17] = tra; data[31,17] = tra; data[32,17] = tra; data[33,17] = tra; data[34,17] = tra; data[35,17] = tra; data[36,17] = tra; data[37,17] = tra; data[38,17] = tra; data[39,17] = tra
        data[0,18] = tra; data[1,18] = tra; data[2,18] = tra; data[3,18] = tra; data[4,18] = tra; data[5,18] = tra; data[6,18] = tra; data[7,18] = tra; data[8,18] = tra; data[9,18] = tra; data[10,18] = tra; data[11,18] = tra; data[12,18] = tra; data[13,18] = tra; data[14,18] = tra; data[15,18] = tra; data[16,18] = bla; data[17,18] = bla; data[18,18] = whi; data[19,18] = whi; data[20,18] = lgr; data[21,18] = lgr; data[22,18] = whi; data[23,18] = whi; data[24,18] = bla; data[25,18] = bla; data[26,18] = tra; data[27,18] = tra; data[28,18] = tra; data[29,18] = tra; data[30,18] = tra; data[31,18] = tra; data[32,18] = tra; data[33,18] = tra; data[34,18] = tra; data[35,18] = tra; data[36,18] = tra; data[37,18] = tra; data[38,18] = tra; data[39,18] = tra
        data[0,19] = tra; data[1,19] = tra; data[2,19] = tra; data[3,19] = tra; data[4,19] = tra; data[5,19] = tra; data[6,19] = tra; data[7,19] = tra; data[8,19] = tra; data[9,19] = tra; data[10,19] = tra; data[11,19] = tra; data[12,19] = tra; data[13,19] = tra; data[14,19] = tra; data[15,19] = tra; data[16,19] = bla; data[17,19] = bla; data[18,19] = whi; data[19,19] = whi; data[20,19] = lgr; data[21,19] = lgr; data[22,19] = whi; data[23,19] = whi; data[24,19] = bla; data[25,19] = bla; data[26,19] = tra; data[27,19] = tra; data[28,19] = tra; data[29,19] = tra; data[30,19] = tra; data[31,19] = tra; data[32,19] = tra; data[33,19] = tra; data[34,19] = tra; data[35,19] = tra; data[36,19] = tra; data[37,19] = tra; data[38,19] = tra; data[39,19] = tra
        data[0,20] = tra; data[1,20] = tra; data[2,20] = tra; data[3,20] = tra; data[4,20] = tra; data[5,20] = tra; data[6,20] = tra; data[7,20] = tra; data[8,20] = tra; data[9,20] = tra; data[10,20] = tra; data[11,20] = tra; data[12,20] = tra; data[13,20] = tra; data[14,20] = bla; data[15,20] = bla; data[16,20] = whi; data[17,20] = whi; data[18,20] = lgr; data[19,20] = lgr; data[20,20] = whi; data[21,20] = whi; data[22,20] = bla; data[23,20] = bla; data[24,20] = tra; data[25,20] = tra; data[26,20] = tra; data[27,20] = tra; data[28,20] = tra; data[29,20] = tra; data[30,20] = tra; data[31,20] = tra; data[32,20] = tra; data[33,20] = tra; data[34,20] = tra; data[35,20] = tra; data[36,20] = tra; data[37,20] = tra; data[38,20] = tra; data[39,20] = tra
        data[0,21] = tra; data[1,21] = tra; data[2,21] = tra; data[3,21] = tra; data[4,21] = tra; data[5,21] = tra; data[6,21] = tra; data[7,21] = tra; data[8,21] = tra; data[9,21] = tra; data[10,21] = tra; data[11,21] = tra; data[12,21] = tra; data[13,21] = tra; data[14,21] = bla; data[15,21] = bla; data[16,21] = whi; data[17,21] = whi; data[18,21] = lgr; data[19,21] = lgr; data[20,21] = whi; data[21,21] = whi; data[22,21] = bla; data[23,21] = bla; data[24,21] = tra; data[25,21] = tra; data[26,21] = tra; data[27,21] = tra; data[28,21] = tra; data[29,21] = tra; data[30,21] = tra; data[31,21] = tra; data[32,21] = tra; data[33,21] = tra; data[34,21] = tra; data[35,21] = tra; data[36,21] = tra; data[37,21] = tra; data[38,21] = tra; data[39,21] = tra
        data[0,22] = tra; data[1,22] = tra; data[2,22] = tra; data[3,22] = tra; data[4,22] = tra; data[5,22] = tra; data[6,22] = tra; data[7,22] = tra; data[8,22] = tra; data[9,22] = tra; data[10,22] = tra; data[11,22] = tra; data[12,22] = bla; data[13,22] = bla; data[14,22] = whi; data[15,22] = whi; data[16,22] = lgr; data[17,22] = lgr; data[18,22] = whi; data[19,22] = whi; data[20,22] = bla; data[21,22] = bla; data[22,22] = tra; data[23,22] = tra; data[24,22] = tra; data[25,22] = tra; data[26,22] = tra; data[27,22] = tra; data[28,22] = tra; data[29,22] = tra; data[30,22] = tra; data[31,22] = tra; data[32,22] = tra; data[33,22] = tra; data[34,22] = tra; data[35,22] = tra; data[36,22] = tra; data[37,22] = tra; data[38,22] = tra; data[39,22] = tra
        data[0,23] = tra; data[1,23] = tra; data[2,23] = tra; data[3,23] = tra; data[4,23] = tra; data[5,23] = tra; data[6,23] = tra; data[7,23] = tra; data[8,23] = tra; data[9,23] = tra; data[10,23] = tra; data[11,23] = tra; data[12,23] = bla; data[13,23] = bla; data[14,23] = whi; data[15,23] = whi; data[16,23] = lgr; data[17,23] = lgr; data[18,23] = whi; data[19,23] = whi; data[20,23] = bla; data[21,23] = bla; data[22,23] = tra; data[23,23] = tra; data[24,23] = tra; data[25,23] = tra; data[26,23] = tra; data[27,23] = tra; data[28,23] = tra; data[29,23] = tra; data[30,23] = tra; data[31,23] = tra; data[32,23] = tra; data[33,23] = tra; data[34,23] = tra; data[35,23] = tra; data[36,23] = tra; data[37,23] = tra; data[38,23] = tra; data[39,23] = tra
        data[0,24] = tra; data[1,24] = tra; data[2,24] = tra; data[3,24] = tra; data[4,24] = tra; data[5,24] = tra; data[6,24] = tra; data[7,24] = tra; data[8,24] = tra; data[9,24] = tra; data[10,24] = bla; data[11,24] = bla; data[12,24] = whi; data[13,24] = whi; data[14,24] = lgr; data[15,24] = lgr; data[16,24] = whi; data[17,24] = whi; data[18,24] = bla; data[19,24] = bla; data[20,24] = tra; data[21,24] = tra; data[22,24] = tra; data[23,24] = tra; data[24,24] = tra; data[25,24] = tra; data[26,24] = tra; data[27,24] = tra; data[28,24] = tra; data[29,24] = tra; data[30,24] = tra; data[31,24] = tra; data[32,24] = tra; data[33,24] = tra; data[34,24] = tra; data[35,24] = tra; data[36,24] = tra; data[37,24] = tra; data[38,24] = tra; data[39,24] = tra
        data[0,25] = tra; data[1,25] = tra; data[2,25] = tra; data[3,25] = tra; data[4,25] = tra; data[5,25] = tra; data[6,25] = tra; data[7,25] = tra; data[8,25] = tra; data[9,25] = tra; data[10,25] = bla; data[11,25] = bla; data[12,25] = whi; data[13,25] = whi; data[14,25] = lgr; data[15,25] = lgr; data[16,25] = whi; data[17,25] = whi; data[18,25] = bla; data[19,25] = bla; data[20,25] = tra; data[21,25] = tra; data[22,25] = tra; data[23,25] = tra; data[24,25] = tra; data[25,25] = tra; data[26,25] = tra; data[27,25] = tra; data[28,25] = tra; data[29,25] = tra; data[30,25] = tra; data[31,25] = tra; data[32,25] = tra; data[33,25] = tra; data[34,25] = tra; data[35,25] = tra; data[36,25] = tra; data[37,25] = tra; data[38,25] = tra; data[39,25] = tra
        data[0,26] = tra; data[1,26] = tra; data[2,26] = tra; data[3,26] = tra; data[4,26] = tra; data[5,26] = tra; data[6,26] = tra; data[7,26] = tra; data[8,26] = bla; data[9,26] = bla; data[10,26] = whi; data[11,26] = whi; data[12,26] = lgr; data[13,26] = lgr; data[14,26] = whi; data[15,26] = whi; data[16,26] = bla; data[17,26] = bla; data[18,26] = tra; data[19,26] = tra; data[20,26] = tra; data[21,26] = tra; data[22,26] = tra; data[23,26] = tra; data[24,26] = tra; data[25,26] = tra; data[26,26] = tra; data[27,26] = tra; data[28,26] = tra; data[29,26] = tra; data[30,26] = tra; data[31,26] = tra; data[32,26] = tra; data[33,26] = tra; data[34,26] = tra; data[35,26] = tra; data[36,26] = tra; data[37,26] = tra; data[38,26] = tra; data[39,26] = tra
        data[0,27] = tra; data[1,27] = tra; data[2,27] = tra; data[3,27] = tra; data[4,27] = tra; data[5,27] = tra; data[6,27] = tra; data[7,27] = tra; data[8,27] = bla; data[9,27] = bla; data[10,27] = whi; data[11,27] = whi; data[12,27] = lgr; data[13,27] = lgr; data[14,27] = whi; data[15,27] = whi; data[16,27] = bla; data[17,27] = bla; data[18,27] = tra; data[19,27] = tra; data[20,27] = tra; data[21,27] = tra; data[22,27] = tra; data[23,27] = tra; data[24,27] = tra; data[25,27] = tra; data[26,27] = tra; data[27,27] = tra; data[28,27] = tra; data[29,27] = tra; data[30,27] = tra; data[31,27] = tra; data[32,27] = tra; data[33,27] = tra; data[34,27] = tra; data[35,27] = tra; data[36,27] = tra; data[37,27] = tra; data[38,27] = tra; data[39,27] = tra
        data[0,28] = tra; data[1,28] = tra; data[2,28] = tra; data[3,28] = tra; data[4,28] = tra; data[5,28] = tra; data[6,28] = bla; data[7,28] = bla; data[8,28] = whi; data[9,28] = whi; data[10,28] = lgr; data[11,28] = lgr; data[12,28] = whi; data[13,28] = whi; data[14,28] = bla; data[15,28] = bla; data[16,28] = tra; data[17,28] = tra; data[18,28] = tra; data[19,28] = tra; data[20,28] = tra; data[21,28] = tra; data[22,28] = tra; data[23,28] = tra; data[24,28] = tra; data[25,28] = tra; data[26,28] = tra; data[27,28] = tra; data[28,28] = tra; data[29,28] = tra; data[30,28] = tra; data[31,28] = tra; data[32,28] = tra; data[33,28] = tra; data[34,28] = tra; data[35,28] = tra; data[36,28] = tra; data[37,28] = tra; data[38,28] = tra; data[39,28] = tra
        data[0,29] = tra; data[1,29] = tra; data[2,29] = tra; data[3,29] = tra; data[4,29] = tra; data[5,29] = tra; data[6,29] = bla; data[7,29] = bla; data[8,29] = whi; data[9,29] = whi; data[10,29] = lgr; data[11,29] = lgr; data[12,29] = whi; data[13,29] = whi; data[14,29] = bla; data[15,29] = bla; data[16,29] = tra; data[17,29] = tra; data[18,29] = tra; data[19,29] = tra; data[20,29] = tra; data[21,29] = tra; data[22,29] = tra; data[23,29] = tra; data[24,29] = tra; data[25,29] = tra; data[26,29] = tra; data[27,29] = tra; data[28,29] = tra; data[29,29] = tra; data[30,29] = tra; data[31,29] = tra; data[32,29] = tra; data[33,29] = tra; data[34,29] = tra; data[35,29] = tra; data[36,29] = tra; data[37,29] = tra; data[38,29] = tra; data[39,29] = tra
        data[0,30] = tra; data[1,30] = tra; data[2,30] = tra; data[3,30] = tra; data[4,30] = bla; data[5,30] = bla; data[6,30] = whi; data[7,30] = whi; data[8,30] = lgr; data[9,30] = lgr; data[10,30] = whi; data[11,30] = whi; data[12,30] = bla; data[13,30] = bla; data[14,30] = tra; data[15,30] = tra; data[16,30] = tra; data[17,30] = tra; data[18,30] = tra; data[19,30] = tra; data[20,30] = tra; data[21,30] = tra; data[22,30] = tra; data[23,30] = tra; data[24,30] = tra; data[25,30] = tra; data[26,30] = tra; data[27,30] = tra; data[28,30] = tra; data[29,30] = tra; data[30,30] = tra; data[31,30] = tra; data[32,30] = tra; data[33,30] = tra; data[34,30] = tra; data[35,30] = tra; data[36,30] = tra; data[37,30] = tra; data[38,30] = tra; data[39,30] = tra
        data[0,31] = tra; data[1,31] = tra; data[2,31] = tra; data[3,31] = tra; data[4,31] = bla; data[5,31] = bla; data[6,31] = whi; data[7,31] = whi; data[8,31] = lgr; data[9,31] = lgr; data[10,31] = whi; data[11,31] = whi; data[12,31] = bla; data[13,31] = bla; data[14,31] = tra; data[15,31] = tra; data[16,31] = tra; data[17,31] = tra; data[18,31] = tra; data[19,31] = tra; data[20,31] = tra; data[21,31] = tra; data[22,31] = tra; data[23,31] = tra; data[24,31] = tra; data[25,31] = tra; data[26,31] = tra; data[27,31] = tra; data[28,31] = tra; data[29,31] = tra; data[30,31] = tra; data[31,31] = tra; data[32,31] = tra; data[33,31] = tra; data[34,31] = tra; data[35,31] = tra; data[36,31] = tra; data[37,31] = tra; data[38,31] = tra; data[39,31] = tra
        data[0,32] = tra; data[1,32] = tra; data[2,32] = bla; data[3,32] = bla; data[4,32] = whi; data[5,32] = whi; data[6,32] = lgr; data[7,32] = lgr; data[8,32] = whi; data[9,32] = whi; data[10,32] = bla; data[11,32] = bla; data[12,32] = tra; data[13,32] = tra; data[14,32] = tra; data[15,32] = tra; data[16,32] = tra; data[17,32] = tra; data[18,32] = tra; data[19,32] = tra; data[20,32] = tra; data[21,32] = tra; data[22,32] = tra; data[23,32] = tra; data[24,32] = tra; data[25,32] = tra; data[26,32] = tra; data[27,32] = tra; data[28,32] = tra; data[29,32] = tra; data[30,32] = tra; data[31,32] = tra; data[32,32] = tra; data[33,32] = tra; data[34,32] = tra; data[35,32] = tra; data[36,32] = tra; data[37,32] = tra; data[38,32] = tra; data[39,32] = tra
        data[0,33] = tra; data[1,33] = tra; data[2,33] = bla; data[3,33] = bla; data[4,33] = whi; data[5,33] = whi; data[6,33] = lgr; data[7,33] = lgr; data[8,33] = whi; data[9,33] = whi; data[10,33] = bla; data[11,33] = bla; data[12,33] = tra; data[13,33] = tra; data[14,33] = tra; data[15,33] = tra; data[16,33] = tra; data[17,33] = tra; data[18,33] = tra; data[19,33] = tra; data[20,33] = tra; data[21,33] = tra; data[22,33] = tra; data[23,33] = tra; data[24,33] = tra; data[25,33] = tra; data[26,33] = tra; data[27,33] = tra; data[28,33] = tra; data[29,33] = tra; data[30,33] = tra; data[31,33] = tra; data[32,33] = tra; data[33,33] = tra; data[34,33] = tra; data[35,33] = tra; data[36,33] = tra; data[37,33] = tra; data[38,33] = tra; data[39,33] = tra
        data[0,34] = bla; data[1,34] = bla; data[2,34] = whi; data[3,34] = whi; data[4,34] = lgr; data[5,34] = lgr; data[6,34] = whi; data[7,34] = whi; data[8,34] = bla; data[9,34] = bla; data[10,34] = tra; data[11,34] = tra; data[12,34] = tra; data[13,34] = tra; data[14,34] = tra; data[15,34] = tra; data[16,34] = tra; data[17,34] = tra; data[18,34] = tra; data[19,34] = tra; data[20,34] = tra; data[21,34] = tra; data[22,34] = tra; data[23,34] = tra; data[24,34] = tra; data[25,34] = tra; data[26,34] = tra; data[27,34] = tra; data[28,34] = tra; data[29,34] = tra; data[30,34] = tra; data[31,34] = tra; data[32,34] = tra; data[33,34] = tra; data[34,34] = tra; data[35,34] = tra; data[36,34] = tra; data[37,34] = tra; data[38,34] = tra; data[39,34] = tra
        data[0,35] = bla; data[1,35] = bla; data[2,35] = whi; data[3,35] = whi; data[4,35] = lgr; data[5,35] = lgr; data[6,35] = whi; data[7,35] = whi; data[8,35] = bla; data[9,35] = bla; data[10,35] = tra; data[11,35] = tra; data[12,35] = tra; data[13,35] = tra; data[14,35] = tra; data[15,35] = tra; data[16,35] = tra; data[17,35] = tra; data[18,35] = tra; data[19,35] = tra; data[20,35] = tra; data[21,35] = tra; data[22,35] = tra; data[23,35] = tra; data[24,35] = tra; data[25,35] = tra; data[26,35] = tra; data[27,35] = tra; data[28,35] = tra; data[29,35] = tra; data[30,35] = tra; data[31,35] = tra; data[32,35] = tra; data[33,35] = tra; data[34,35] = tra; data[35,35] = tra; data[36,35] = tra; data[37,35] = tra; data[38,35] = tra; data[39,35] = tra
        data[0,36] = bla; data[1,36] = bla; data[2,36] = lgr; data[3,36] = lgr; data[4,36] = whi; data[5,36] = whi; data[6,36] = bla; data[7,36] = bla; data[8,36] = tra; data[9,36] = tra; data[10,36] = tra; data[11,36] = tra; data[12,36] = tra; data[13,36] = tra; data[14,36] = tra; data[15,36] = tra; data[16,36] = tra; data[17,36] = tra; data[18,36] = tra; data[19,36] = tra; data[20,36] = tra; data[21,36] = tra; data[22,36] = tra; data[23,36] = tra; data[24,36] = tra; data[25,36] = tra; data[26,36] = tra; data[27,36] = tra; data[28,36] = tra; data[29,36] = tra; data[30,36] = tra; data[31,36] = tra; data[32,36] = tra; data[33,36] = tra; data[34,36] = tra; data[35,36] = tra; data[36,36] = tra; data[37,36] = tra; data[38,36] = tra; data[39,36] = tra
        data[0,37] = bla; data[1,37] = bla; data[2,37] = lgr; data[3,37] = lgr; data[4,37] = whi; data[5,37] = whi; data[6,37] = bla; data[7,37] = bla; data[8,37] = tra; data[9,37] = tra; data[10,37] = tra; data[11,37] = tra; data[12,37] = tra; data[13,37] = tra; data[14,37] = tra; data[15,37] = tra; data[16,37] = tra; data[17,37] = tra; data[18,37] = tra; data[19,37] = tra; data[20,37] = tra; data[21,37] = tra; data[22,37] = tra; data[23,37] = tra; data[24,37] = tra; data[25,37] = tra; data[26,37] = tra; data[27,37] = tra; data[28,37] = tra; data[29,37] = tra; data[30,37] = tra; data[31,37] = tra; data[32,37] = tra; data[33,37] = tra; data[34,37] = tra; data[35,37] = tra; data[36,37] = tra; data[37,37] = tra; data[38,37] = tra; data[39,37] = tra
        data[0,38] = bla; data[1,38] = bla; data[2,38] = bla; data[3,38] = bla; data[4,38] = bla; data[5,38] = bla; data[6,38] = tra; data[7,38] = tra; data[8,38] = tra; data[9,38] = tra; data[10,38] = tra; data[11,38] = tra; data[12,38] = tra; data[13,38] = tra; data[14,38] = tra; data[15,38] = tra; data[16,38] = tra; data[17,38] = tra; data[18,38] = tra; data[19,38] = tra; data[20,38] = tra; data[21,38] = tra; data[22,38] = tra; data[23,38] = tra; data[24,38] = tra; data[25,38] = tra; data[26,38] = tra; data[27,38] = tra; data[28,38] = tra; data[29,38] = tra; data[30,38] = tra; data[31,38] = tra; data[32,38] = tra; data[33,38] = tra; data[34,38] = tra; data[35,38] = tra; data[36,38] = tra; data[37,38] = tra; data[38,38] = tra; data[39,38] = tra
        data[0,39] = bla; data[1,39] = bla; data[2,39] = bla; data[3,39] = bla; data[4,39] = bla; data[5,39] = bla; data[6,39] = tra; data[7,39] = tra; data[8,39] = tra; data[9,39] = tra; data[10,39] = tra; data[11,39] = tra; data[12,39] = tra; data[13,39] = tra; data[14,39] = tra; data[15,39] = tra; data[16,39] = tra; data[17,39] = tra; data[18,39] = tra; data[19,39] = tra; data[20,39] = tra; data[21,39] = tra; data[22,39] = tra; data[23,39] = tra; data[24,39] = tra; data[25,39] = tra; data[26,39] = tra; data[27,39] = tra; data[28,39] = tra; data[29,39] = tra; data[30,39] = tra; data[31,39] = tra; data[32,39] = tra; data[33,39] = tra; data[34,39] = tra; data[35,39] = tra; data[36,39] = tra; data[37,39] = tra; data[38,39] = tra; data[39,39] = tra
        fd = os.path.join(Mn, Ite, It + '.png')
        imageio.imwrite(fd, data)  
        
        # Generates the main cs file
        MnMain = os.path.join(Mn, Mn + ".cs")
        Mncs = open(MnMain, "w")
        Mncs.write("using Terraria.ModLoader;" + nl + nl + "namespace " + Mn + nl + '{' + nl + '    class ' + Mn + ' : Mod' + nl + '	{' + nl + '		public ' + Mn + '()' + nl)
        Mncs.write("		{" + nl + "		}" + nl + '	}' + nl + '}')
        
        # Generates the .csproj file with build params
        Mnproj = os.path.join(Mn, Mn + ".csproj")
        Mnpr = open(Mnproj, "w")
        Mnpr.write('<?xml version="1.0" encoding="utf-8"?>' + nl + '<Project ToolsVersion="14.0" DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">' + nl)
        Mnpr.write("""  <Import Project="$(MSBuildExtensionsPath)$(MSBuildToolsVersion)\\Microsoft.Common.props" Condition="Exists('$(MSBuildExtensionsPath)$(MSBuildToolsVersion)\\Microsoft.Common.props')" />""" + nl)
        Mnpr.write("  <PropertyGroup>" + nl + """    <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>""" + nl + """    <Platform Condition=" '$(Platform)' == '' ">AnyCPU</Platform>""" + nl)
        Mnpr.write("    <ProjectGuid>{8298EAB6-0586-4BDA-9483-83624B66B13A}</ProjectGuid>" + nl + "    <OutputType>Library</OutputType>" + nl + "    <AppDesignerFolder>Properties</AppDesignerFolder>" + nl)
        Mnpr.write("    <RootNamespace>" + Mn + "</RootNamespace>" + nl + "    <AssemblyName>" + Mn + "</AssemblyName>" + nl + "    <TargetFrameworkVersion>v4.5.2</TargetFrameworkVersion>" + nl)
        Mnpr.write("    <FileAlignment>512</FileAlignment>" + nl + "    <AutoGenerateBindingRedirects>true</AutoGenerateBindingRedirects>" + nl + "  </PropertyGroup>" + nl + """  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">""" + nl)
        Mnpr.write("    <PlatformTarget>AnyCPU</PlatformTarget>" + nl + "    <DebugSymbols>true</DebugSymbols>" + nl + "    <DebugType>full</DebugType>" + nl + "    <Optimize>false</Optimize>" + nl)
        Mnpr.write("    <OutputPath>bin\\Debug\\</OutputPath>" + nl + "    <DefineConstants>DEBUG;TRACE</DefineConstants>" + nl + "    <ErrorReport>prompt</ErrorReport>" + nl + "    <WarningLevel>4</WarningLevel>" + nl)
        Mnpr.write("  </PropertyGroup>" + nl + """  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">""" + nl + "    <PlatformTarget>AnyCPU</PlatformTarget>" + nl + "    <DebugType>pdbonly</DebugType>" + nl)
        Mnpr.write("    <Optimize>true</Optimize>" + nl + "    <OutputPath>bin\\Release\\</OutputPath>" + nl + "    <DefineConstants>TRACE</DefineConstants>" + nl + "    <ErrorReport>prompt</ErrorReport>" + nl)
        Mnpr.write("    <WarningLevel>4</WarningLevel>" + nl + "  </PropertyGroup>" + nl + "  <ItemGroup>" + nl + '    <Compile Include="**\\*.cs" />' + nl + "  </ItemGroup>" + nl + "  <ItemGroup>" + nl)
        Mnpr.write('    <Reference Include="Microsoft.Xna.Framework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=842cf8be1de50553, processorArchitecture=x86">' + nl + "      <SpecificVersion>False</SpecificVersion>" + nl)
        Mnpr.write("      <HintPath>C:\\Windows\\Microsoft.NET\\assembly\\GAC_32\\Microsoft.Xna.Framework\\v4.0_4.0.0.0__842cf8be1de50553\\Microsoft.Xna.Framework.dll</HintPath>" + nl + "    </Reference>" + nl)
        Mnpr.write('    <Reference Include="Microsoft.Xna.Framework.Game, Version=4.0.0.0, Culture=neutral, PublicKeyToken=842cf8be1de50553, processorArchitecture=x86">' + nl + "      <SpecificVersion>False</SpecificVersion>" + nl)
        Mnpr.write('      <HintPath>C:\\Windows\\Microsoft.NET\\assembly\\GAC_32\\Microsoft.Xna.Framework.Game\\v4.0_4.0.0.0__842cf8be1de50553\\Microsoft.Xna.Framework.Game.dll</HintPath>' + nl + '    </Reference>' + nl)
        Mnpr.write('    <Reference Include="Microsoft.Xna.Framework.Graphics, Version=4.0.0.0, Culture=neutral, PublicKeyToken=842cf8be1de50553, processorArchitecture=x86">' + nl + '      <SpecificVersion>False</SpecificVersion>' + nl)
        Mnpr.write('      <HintPath>C:\\Windows\\Microsoft.NET\\assembly\\GAC_32\\Microsoft.Xna.Framework.Graphics\\v4.0_4.0.0.0__842cf8be1de50553\\Microsoft.Xna.Framework.Graphics.dll</HintPath>' + nl + '    </Reference>' + nl)
        Mnpr.write('    <Reference Include="Microsoft.Xna.Framework.Xact, Version=4.0.0.0, Culture=neutral, PublicKeyToken=842cf8be1de50553, processorArchitecture=x86">' + nl + '      <SpecificVersion>False</SpecificVersion>' + nl)
        Mnpr.write('      <HintPath>C:\\Windows\\Microsoft.NET\\assembly\\GAC_32\\Microsoft.Xna.Framework.Xact\\v4.0_4.0.0.0__842cf8be1de50553\\Microsoft.Xna.Framework.Xact.dll</HintPath>' + nl + '    </Reference>' + nl)
        Mnpr.write('    <Reference Include="System" />' + nl + '    <Reference Include="Terraria">' + nl + '      <HintPath>C:\\Program Files (x86)\\Steam\\steamapps\\common\\terraria\\Terraria.exe</HintPath>' + nl + '    </Reference>' + nl)
        Mnpr.write('  </ItemGroup>' + nl + '  <Import Project="$(MSBuildToolsPath)\\Microsoft.CSharp.targets" />' + nl + '  <PropertyGroup>' + nl + """   <PostBuildEvent>"C:\\Program Files (x86)\\Steam\\steamapps\\common\\terraria\\Terraria.exe" -build "$(ProjectDir)\\" -eac "$(TargetPath)"</PostBuildEvent>""" + nl)
        Mnpr.write('  </PropertyGroup>' + nl + '</Project>')
        
        # Generates the csproj.user file
        Mnproju = os.path.join(Mn, Mn + ".csproj.user")
        Mnpru = open(Mnproju, "w")
        Mnpru.write('<?xml version="1.0" encoding="utf-8"?>' + nl + '<Project ToolsVersion="14.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">' + nl)
        Mnpru.write("""  <PropertyGroup Condition="'$(Configuration)|$(Platform)' == 'Debug|AnyCPU'">""" + nl)
        Mnpru.write("    <StartAction>Program</StartAction>" + nl + "    <StartProgram>D:\\Steam\\steamapps\\common\\Terraria\\Terraria.exe</StartProgram>" + nl)
        Mnpru.write("    <StartWorkingDirectory>D:\\Steam\\steamapps\\common\\Terraria\\</StartWorkingDirectory>" + nl + "  </PropertyGroup>" + nl + "</Project>" + nl)
        print "\nDone!"
        os.system("pause")
        sys.exit(0)
    else:
        # Clears the console and prints ASCI art, credits and prints an error.
        clear = lambda: os.system('cls')
        clear()
        print "  __  __           _    _____ _        _      _                 _____                           _             " + '\n' + " |  \\/  |         | |  / ____| |      | |    | |               / ____|                         | |            " + '\n' + " | \\  / | ___   __| | | (___ | | _____| | ___| |_ ___  _ __   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ " + '\n' + " | |\\/| |/ _ \\ / _` |  \\___ \\| |/ / _ \\ |/ _ \\ __/ _ \\| '_ \\  | | |_ |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|" + '\n' + " | |  | | (_) | (_| |  ____) |   <  __/ |  __/ || (_) | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   " + '\n' + " |_|  |_|\\___/ \\__,_| |_____/|_|\\_\\___|_|\\___|\\__\\___/|_| |_|  \\_____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   \n"
        print "Created by ProjectET.\nOriginal mod skeleton generator by jopojelly."
        print "--------------------------------------------------------------------------\n"
        print "ERROR | Following field(s) are empty.\n-----------------------------------"
    
    # Prints which field are errors by checking which one didnt assign a 1 to the z, x, c, or v variable.
    if z != 1:
        print erz
    if x != 1:
        print erx
    if c != 1:
        print erc
    if v != 1:
        print erv
    print ""
    os.system("pause")
    sys.exit(0)

elif In == "quit":
    sys.exit(0)

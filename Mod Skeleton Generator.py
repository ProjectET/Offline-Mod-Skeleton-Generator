import os
import sys

os.system("title Mod Skeleton Generator")
print "  __  __           _    _____ _        _      _                 _____                           _             " + '\n' + " |  \\/  |         | |  / ____| |      | |    | |               / ____|                         | |            " + '\n' + " | \\  / | ___   __| | | (___ | | _____| | ___| |_ ___  _ __   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ " + '\n' + " | |\\/| |/ _ \\ / _` |  \\___ \\| |/ / _ \\ |/ _ \\ __/ _ \\| '_ \\  | | |_ |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|" + '\n' + " | |  | | (_) | (_| |  ____) |   <  __/ |  __/ || (_) | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   " + '\n' + " |_|  |_|\\___/ \\__,_| |_____/|_|\\_\\___|_|\\___|\\__\\___/|_| |_|  \\_____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   \n"
print "Created by ProjectET.\nOriginal mod skeleton generator by jopojelly."
print "--------------------------------------------------------------------------\n"

options = ["generate", "quit"]
while True:
    In = raw_input("To begin generating files type 'generate', to close the generator type 'quit': ")
    if In in options: 
        break
    elif In == "":
        print "No command entered. Enter 'generate' or 'quit'.\n"
    else:
        print "Invalid command. Enter 'generate' or 'quit'.\n"

if In == "generate":
    clear = lambda: os.system('cls')
    clear()
    print "  __  __           _    _____ _        _      _                 _____                           _             " + '\n' + " |  \\/  |         | |  / ____| |      | |    | |               / ____|                         | |            " + '\n' + " | \\  / | ___   __| | | (___ | | _____| | ___| |_ ___  _ __   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ " + '\n' + " | |\\/| |/ _ \\ / _` |  \\___ \\| |/ / _ \\ |/ _ \\ __/ _ \\| '_ \\  | | |_ |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|" + '\n' + " | |  | | (_) | (_| |  ____) |   <  __/ |  __/ || (_) | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   " + '\n' + " |_|  |_|\\___/ \\__,_| |_____/|_|\\_\\___|_|\\___|\\__\\___/|_| |_|  \\_____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   \n"
    print "Created by ProjectET.\nOriginal mod skeleton generator by jopojelly."
    print "--------------------------------------------------------------------------\n"
    print "For Mod Name and 1st Item's Name, don't use apostrophes or other special characters.\n"
    z = 0
    x = 0
    c = 0
    v = 0
    erz = ""
    erx = ""
    erc = ""
    erv = ""
    Ite = "Items"
    
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

    b = z + x + c + v
    if b == 4:
        os.makedirs(os.path.join(Mn, Ite))
        nl = '\n'
        buildtxt = os.path.join(Mn, "build.txt")
        build = open(buildtxt, "w")
        build.write("author = " + MA + nl)
        build.write("version = 0.1" + nl)
        build.write("displayName = " + Md)
                
        desctxt = os.path.join(Mn, "description.txt")
        desc = open(desctxt, "w")
        desc.write(Md + " is a pretty cool mod, it does...this. Modify this file with a description of your mod.")

        Itemcs = os.path.join(Mn, "Items", It + '.cs')
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

        Itempng = os.path.join(Mn, "Items",  'README.txt')
        Itpn = open(Itempng, "w")
        Itpn.write("There should be a sword texture, however I do not know how to generate an image in Python 2.7.\nUntil then use PAINT.net or any other image creation software that allows transparancy to create a sword image 40x40 pixels..\nThanks for using my generator.\n\n-ProjectET")

        MnMain = os.path.join(Mn, Mn + ".cs")
        Mncs = open(MnMain, "w")
        Mncs.write("using Terraria.ModLoader;" + nl + nl + "namespace " + Mn + nl + '{' + nl + '    class ' + Mn + ' : Mod' + nl + '	{' + nl + '		public ' + Mn + '()' + nl)
        Mncs.write("		{" + nl + "		}" + nl + '	}' + nl + '}')

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
        clear = lambda: os.system('cls')
        clear()
        print "  __  __           _    _____ _        _      _                 _____                           _             " + '\n' + " |  \\/  |         | |  / ____| |      | |    | |               / ____|                         | |            " + '\n' + " | \\  / | ___   __| | | (___ | | _____| | ___| |_ ___  _ __   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ " + '\n' + " | |\\/| |/ _ \\ / _` |  \\___ \\| |/ / _ \\ |/ _ \\ __/ _ \\| '_ \\  | | |_ |/ _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|" + '\n' + " | |  | | (_) | (_| |  ____) |   <  __/ |  __/ || (_) | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   " + '\n' + " |_|  |_|\\___/ \\__,_| |_____/|_|\\_\\___|_|\\___|\\__\\___/|_| |_|  \\_____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   \n"
        print "Created by ProjectET.\nOriginal mod skeleton generator by jopojelly."
        print "--------------------------------------------------------------------------\n"
        print "ERROR | Following field(s) are empty.\n-----------------------------------"
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
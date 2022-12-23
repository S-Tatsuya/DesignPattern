using System;
using Entities;
using Command;

internal class Program
{
    private static void Main(string[] args)
    {
        // runSimpleRemoteControl();
        // runRemoteControl();
        // undoRemoteControl();
        // undoRemoteControlFan();
        macroCommand();
    }

    private static void macroCommand()
    {
        var light = new Light("リビングルーム");
        var garageDoor = new GarageDoor();
        var stereo = new Stereo();
        var ceilingFan = new CeilingFan("リビングルーム");

        var lightOn = new LightOnCommand(light);
        var garageDoorOpne = new GarageDoorOpenCommand(garageDoor);
        var stereoOnWithCD = new StereoOnWithCDCommand(stereo);
        var ceilingFanHigh = new CeilingFanHighCommnad(ceilingFan);
        ICommand[] partyOn = { lightOn, garageDoorOpne, stereoOnWithCD, ceilingFanHigh };

        var lightOff = new LightOffCommand(light);
        var garageDoorClose = new GarageDoorCloseCommand(garageDoor);
        var stereoOff = new StereoOffCommand(stereo);
        var ceilingOff = new CeilingFanOffCommand(ceilingFan);
        ICommand[] partyOff = { lightOff, garageDoorClose, stereoOff, ceilingOff };

        var partyOnMacro = new MacroCommand(partyOn);
        var partyOffMacro = new MacroCommand(partyOff);

        var remoteControl = new RemoteControl();

        remoteControl.setCommand(0, partyOnMacro, partyOffMacro);

        Console.WriteLine("---------マクロON");
        remoteControl.onButtonWasPushed(0);
        Console.WriteLine("---------マクロOFF");
        remoteControl.offButtonWasPushed(0);
        Console.WriteLine("---------マクロUndo");
        remoteControl.undoButtonWasPushed();
    }

    private static void undoRemoteControlFan()
    {
        RemoteControl remoteControl = new RemoteControl();

        CeilingFan ceilingFan = new CeilingFan("リビングルーム");

        CeilingFanHighCommnad ceilingFanHigh = new CeilingFanHighCommnad(ceilingFan);
        CeilingFanMediumCommand ceilingFanMedium = new CeilingFanMediumCommand(ceilingFan);
        CeilingFanLowCommand ceilingFanLow = new CeilingFanLowCommand(ceilingFan);
        CeilingFanOffCommand ceilingFanOff = new CeilingFanOffCommand(ceilingFan);

        remoteControl.setCommand(0, ceilingFanMedium, ceilingFanOff);
        remoteControl.setCommand(1, ceilingFanHigh, ceilingFanOff);
        remoteControl.setCommand(2, ceilingFanLow, ceilingFanOff);

        remoteControl.onButtonWasPushed(0);
        remoteControl.offButtonWasPushed(0);
        Console.WriteLine(remoteControl);
        remoteControl.undoButtonWasPushed();

        remoteControl.onButtonWasPushed(1);
        Console.WriteLine(remoteControl);
        remoteControl.undoButtonWasPushed();

        remoteControl.onButtonWasPushed(2);
        remoteControl.onButtonWasPushed(1);
        Console.WriteLine(remoteControl);
        remoteControl.undoButtonWasPushed();

    }

    private static void undoRemoteControl()
    {
        RemoteControl remoteControl = new RemoteControl();

        Light livingRoomLight = new Light("リビングルーム");
        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);

        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);

        remoteControl.onButtonWasPushed(0);
        remoteControl.offButtonWasPushed(0);
        Console.WriteLine(remoteControl);

        remoteControl.undoButtonWasPushed();
        remoteControl.offButtonWasPushed(0);
        remoteControl.onButtonWasPushed(0);
        Console.WriteLine(remoteControl);

        remoteControl.undoButtonWasPushed();
    }

    private static void runRemoteControl()
    {
        RemoteControl remoteControl = new RemoteControl();

        Light livingRoomLight = new Light("リビングルーム");
        Light kitchenLight = new Light("キッチン");
        CeilingFan ceilingFan = new CeilingFan("リビングルーム");
        GarageDoor garageDoor = new GarageDoor();
        Stereo stereo = new Stereo();

        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
        LightOnCommand kitchenLightOn = new LightOnCommand(kitchenLight);
        LightOffCommand kitchenLightOff = new LightOffCommand(kitchenLight);

        CeilingFanHighCommnad ceilingFanOn = new CeilingFanHighCommnad(ceilingFan);
        CeilingFanOffCommand ceilingFanOff = new CeilingFanOffCommand(ceilingFan);

        GarageDoorOpenCommand garageDoorOpne = new GarageDoorOpenCommand(garageDoor);
        GarageDoorCloseCommand garageDoorClose = new GarageDoorCloseCommand(garageDoor);

        StereoOnWithCDCommand stereoOnWithCD = new StereoOnWithCDCommand(stereo);
        StereoOffCommand stereoOff = new StereoOffCommand(stereo);

        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff);
        remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff);
        remoteControl.setCommand(3, garageDoorOpne, garageDoorClose);
        remoteControl.setCommand(4, stereoOnWithCD, stereoOff);

        Console.WriteLine(remoteControl);

        remoteControl.onButtonWasPushed(0);
        remoteControl.offButtonWasPushed(0);
        remoteControl.onButtonWasPushed(1);
        remoteControl.offButtonWasPushed(1);
        remoteControl.onButtonWasPushed(2);
        remoteControl.offButtonWasPushed(2);
        remoteControl.onButtonWasPushed(3);
        remoteControl.offButtonWasPushed(3);
        remoteControl.onButtonWasPushed(4);
        remoteControl.offButtonWasPushed(4);
        remoteControl.onButtonWasPushed(5);
        remoteControl.offButtonWasPushed(6);
    }

    private static void runSimpleRemoteControl()
    {
        Light light = new Light("テスト");
        LightOnCommand lightOn = new LightOnCommand(light);
        SimpleRemoteControl remote = new SimpleRemoteControl(lightOn);

        remote.setCommand(lightOn);
        remote.buttonWasPressed();

        GarageDoor garageDoor = new GarageDoor();
        GarageDoorOpenCommand grageOpen = new GarageDoorOpenCommand(garageDoor);

        remote.setCommand(grageOpen);
        remote.buttonWasPressed();
    }
}

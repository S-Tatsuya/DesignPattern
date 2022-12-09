using System;
using Entities;
using Command;

internal class Program
{
    private static void Main(string[] args)
    {
        // runSimpleRemoteControl();
        runRemoteControl();
    }

    private static void runRemoteControl()
    {
        RemoteControl remoteControl = new RemoteControl();

        Light livingRoomLight = new Light("リビングルーム");
        Light kitchenLight = new Light("キッチン");
        CeilingFan ceilingFan = new CeilingFan();
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

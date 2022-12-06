using System;
using Entities;
using Command;

internal class Program
{
    private static void Main(string[] args)
    {
        Light light = new Light();
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

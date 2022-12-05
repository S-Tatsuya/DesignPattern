using System;
using Entities;
using Command;

internal class Program
{
    private static void Main(string[] args)
    {
        SimpleRemoteControl remote = new SimpleRemoteControl();
        Light light = new Light();
        LightOnCommand lightOn = new LightOnCommand(light);

        remote.setCommand(lightOn);
        remote.buttonWasPressed();
    }

    private string GetDebuggerDisplay()
    {
        return ToString();
    }
}

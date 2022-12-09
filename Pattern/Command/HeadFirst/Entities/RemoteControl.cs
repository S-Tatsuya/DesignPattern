using System;
using Command;
using System.Text;

namespace Entities
{
    public class RemoteControl {
        ICommand[] onCommands;
        ICommand[] offCommands;

        public RemoteControl()
        {
            onCommands = new ICommand[7];
            offCommands = new ICommand[7];

            ICommand noCommand = new NoCommand();
            for (int i = 0; i < onCommands.Length ; i++)
            {
                onCommands[i] = noCommand;
                offCommands[i] = noCommand;
            }
        }

        public void setCommand(int slot, ICommand onCommand, ICommand offCommand)
        {
            onCommands[slot] = onCommand;
            offCommands[slot] = offCommand;
        }

        public void onButtonWasPushed(int slot)
        {
            onCommands[slot].execute();
        }

        public void offButtonWasPushed(int slot)
        {
            offCommands[slot].execute();
        }

        public override String ToString()
        {
            StringBuilder stringBuff = new StringBuilder();
            stringBuff.Append("\n------ リモコン ------\n");
            for (int i = 0; i < onCommands.Length; i++)
            {
                stringBuff.Append("[スロット" + i + "]" + onCommands[i].GetType().Name + " " + offCommands[i].GetType().Name + "\n");
            }

            return stringBuff.ToString();
        }
    }
}

using System;
using Command;
using System.Text;

namespace Entities
{
    public class RemoteControl {
        ICommand[] onCommands;
        ICommand[] offCommands;
        ICommand undoCommand;

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

            undoCommand = noCommand;
        }

        public void setCommand(int slot, ICommand onCommand, ICommand offCommand)
        {
            onCommands[slot] = onCommand;
            offCommands[slot] = offCommand;
        }

        public void onButtonWasPushed(int slot)
        {
            onCommands[slot].execute();
            undoCommand = onCommands[slot];
        }

        public void offButtonWasPushed(int slot)
        {
            offCommands[slot].execute();
            undoCommand = offCommands[slot];
        }

        public void undoButtonWasPushed()
        {
            undoCommand.undo();
        }

        public override String ToString()
        {
            StringBuilder stringBuff = new StringBuilder();
            stringBuff.Append("\n------ リモコン ------\n");
            for (int i = 0; i < onCommands.Length; i++)
            {
                stringBuff.Append("[スロット" + i + "]" + onCommands[i].GetType().Name + " " + offCommands[i].GetType().Name + "\n");
            }
            
            stringBuff.Append("[アンドゥ]" + undoCommand.GetType().Name);

            return stringBuff.ToString();
        }
    }
}

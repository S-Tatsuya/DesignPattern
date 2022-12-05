using System;
using Command;

namespace Entities
{
    public class SimpleRemoteControl 
    {
        ICommand slot;

        public SimpleRemoteControl()
        {
        }

        public void setCommand(ICommand command)
        {
            slot = command;
        }

        public void buttonWasPressed()
        {
            slot.execute();
        }
    } 
}

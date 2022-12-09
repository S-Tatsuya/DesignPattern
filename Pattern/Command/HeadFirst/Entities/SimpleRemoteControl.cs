using Command;

namespace Entities
{
    public class SimpleRemoteControl 
    {
        ICommand _slot;

        public SimpleRemoteControl(ICommand command)
        {
            _slot = command;
        }

        public void setCommand(ICommand command)
        {
            _slot = command;
        }

        public void buttonWasPressed()
        {
            _slot.execute();
        }
    } 
}

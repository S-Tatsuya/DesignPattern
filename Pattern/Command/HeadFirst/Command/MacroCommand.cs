namespace Command
{
    public class MacroCommand : ICommand
    {
        ICommand[] _commands;

        public MacroCommand(ICommand[] commands)
        {
            _commands = commands;
        }

        public void execute()
        {
            foreach (var item in _commands)
            {
               item.execute(); 
            }
        }

        public void undo()
        {
            foreach (var item in _commands)
            {
               item.undo(); 
            }
        }
    }
}

using System;

namespace Command
{
    public class NoCommand : ICommand
    {
        public NoCommand()
        {
        }

        public void execute()
        {
            Console.WriteLine("処理なし");
        }
    }
}

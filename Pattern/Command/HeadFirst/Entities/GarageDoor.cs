using System;

namespace Entities
{
    public class GarageDoor
    {
        public GarageDoor()
        {
        }

        public void up()
        {
            Console.WriteLine("GarageDoor UP");
        }

        public void down()
        {
            Console.WriteLine("GarageDoor DOWN");
        }

        public void stop()
        {
            Console.WriteLine("GarageDoor STOP");
        }

        public void lightOn()
        {
            Console.WriteLine("GarageDoor Light ON");
        }

        public void lightOff()
        {
            Console.WriteLine("GarageDoor Light OFF");
        }
    }
}

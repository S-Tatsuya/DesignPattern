using System;

namespace Entities
{
    public class Light
    {
        String _name;

        public Light(String name)
        {
            _name = name;
        }

        public void on()
        {
            Console.WriteLine(_name + " Light On");
        }
        
        public void off()
        {
            Console.WriteLine(_name + "Light Off");
        }
    }
}

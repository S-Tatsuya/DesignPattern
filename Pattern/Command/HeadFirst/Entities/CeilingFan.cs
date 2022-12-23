using System;

namespace Entities
{
    public class CeilingFan
    {
        public static int HIGH = 3;
        public static int MEDIUM = 2;
        public static int LOW = 1;
        public static int OFF = 0;
        private String _location;
        private int _speed;

        public CeilingFan(String location)
        {
            _location = location;
            _speed = OFF;
        }

        public int Speed
        {
            get { return _speed; }
        }

        public void high()
        {
            _speed = HIGH;
            Console.WriteLine("Ceiling Fan High");
        }

        public void medium()
        {
            _speed = MEDIUM;
            Console.WriteLine("Ceiling Fan Medium");
        }

        public void low()
        {
            _speed = LOW;
            Console.WriteLine("Ceiling Fan Low");
        }

        public void off()
        {
            _speed = OFF;
            Console.WriteLine("Ceiling Fan Off");
        }
    }
}

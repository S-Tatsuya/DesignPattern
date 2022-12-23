using System;

namespace Entities
{
    public class Stereo
    {
        public Stereo()
        {
        }

        public void on()
        {
            Console.WriteLine("Stereo On");
        }

        public void off()
        {
            Console.WriteLine("Stereo Off");
        }

        public void setCd()
        {
            Console.WriteLine("Stereo Set CD");
        }

        public void setDvd()
        {
            Console.WriteLine("Stereo Set DVD");
        }

        public void setRaidio()
        {
            Console.WriteLine("Stereo Set Raidio");
        }

        public void setVolume()
        {
            Console.WriteLine("Stereo Set Volume");
        }
    }
}

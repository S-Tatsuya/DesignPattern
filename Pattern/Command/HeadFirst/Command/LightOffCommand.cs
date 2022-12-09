using Entities;

namespace Command
{

    public class LightOffCommand : ICommand
    {
        Light _light;
        public LightOffCommand(Light light)
        {
            _light = light;
        }

        public void execute()
        {
            _light.off();
        }

        public void undo()
        {
            _light.on();
        }
    }
}

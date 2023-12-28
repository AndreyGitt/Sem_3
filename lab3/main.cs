
using System;

namespace Tanks
{
    abstract class Tank
    {
        protected int health;
        protected int speed;
        protected int damage;

        public Tank(int health, int speed, int damage)
        {
            this.health = health;
            this.speed = speed;
            this.damage = damage;
        }

        public abstract void Fire();

        public virtual void Move()
        {
            Console.WriteLine($"Moving at a speed of {speed} km/h");
        }

        public override string ToString()
        {
            return $"Health: {health}, Speed: {speed}, Damage: {damage}";
        }
    }

    class HeavyTank : Tank, IPrint
    {
        public HeavyTank(int health, int speed, int damage) : base(health, speed, damage)
        {
        }

        public override void Fire()
        {
            Console.WriteLine($"Shooting a heavy bullet with {damage} damage");
        }

        public override void Move()
        {
            Console.WriteLine($"Moving slowly at {speed} km/h");
        }

        public void Print()
        {
            Console.WriteLine($"Heavy Tank: {base.ToString()}");
        }
    }

    class MediumTank : Tank, IPrint
    {
        public MediumTank(int health, int speed, int damage) : base(health, speed, damage)
        {
        }
        public override void Fire()
        {
            Console.WriteLine($"Shooting a bullet with {damage} damage");
        }
        public void Print()
        {
            Console.WriteLine($"Medium Tank: {base.ToString()}");
        }
    }

    class LightTank : Tank, IPrint
    {
        public LightTank(int health, int speed, int damage) : base(health, speed, damage)
        {
        }

        public override void Fire()
        {
            Console.WriteLine($"Shooting a light bullet with {damage} damage");
        }

        public override void Move()
        {
            Console.WriteLine($"Moving fast at {speed} km/h");
        }

        public void Print()
        {
            Console.WriteLine($"Light Tank: {base.ToString()}");
        }
    }

    interface IPrint
    {
        void Print();
    }

    class Program
    {
        static void Main(string[] args)
        {
            HeavyTank heavy = new HeavyTank(1000, 30, 500);
            heavy.Fire();
            heavy.Move();
            heavy.Print();

            MediumTank medium = new MediumTank(500, 50, 250);
            medium.Fire();
            medium.Move();
            medium.Print();

            LightTank light = new LightTank(200, 80, 100);
            light.Fire();
            light.Move();
            light.Print();

            Console.ReadKey();
        }
    }
}
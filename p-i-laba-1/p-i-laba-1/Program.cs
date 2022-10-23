namespace exp_1
{
    internal class SomeClass
    {
        public int X { get; set; }
        public int Y { get; set; }
        public int Z { get; set; }

        public SomeClass()
        {
            this.X = 0;
            this.Y = 0;
            this.Z = 0;
        }

        public SomeClass(int X, int Y, int Z)
        {
            this.X = X;
            this.Y = Y;
            this.Z = Z;
        }

        // copy constructor
        public SomeClass(SomeClass someObject)
        {
            this.X = someObject.X;
            this.Y = someObject.Y;
            this.Z = someObject.Z;
        }

        // clone method
        public SomeClass Clone()
        {
            return new SomeClass(this.X, this.Y, this.Z);
        }

        public override string ToString()
        {
            return
                String.Format(
                    "SomeClass X: {0}; Y: {1}; Z: {2};\nhashCode: {3}\n",
                    this.X, this.Y, this.Z, this.GetHashCode()
                );
        }
    }


    internal class Program
    {
        private static void Main()
        {
            Console.Write("X: ");
            int X = Convert.ToInt32(Console.ReadLine());
            Console.Write("Y: ");
            int Y = Convert.ToInt32(Console.ReadLine());
            Console.Write("Z: ");
            int Z = Convert.ToInt32(Console.ReadLine());

            var someObject1 = new SomeClass(X, Y, Z);
            var someObject12 = someObject1;
            var someObject2 = new SomeClass();
            var someObject3 = new SomeClass(someObject1);
            var someObject4 = someObject2.Clone();

            Console.WriteLine(someObject1);
            Console.WriteLine(someObject12);
            Console.WriteLine(someObject2);
            Console.WriteLine(someObject3);
            Console.WriteLine(someObject4);

            Console.ReadLine();
        }
    }
}
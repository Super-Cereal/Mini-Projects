namespace exp_2
{
    internal class SomeClass
    {
        public int pos { get; set; }

        public SomeClass(int pos)
        {
            this.pos = pos;
        }

        public override string ToString() {
            return
                String.Format(
                    "SomeClass on position {0}",
                    this.pos
                );
        }
    }

    internal class Program
    {
        private static void Main()
        {
            const int N = 5;

            // создаем коллекцию 5 обьектов
            var array = new List<object>(N);
            for (int i = 0; i < N; i += 1)
            {
                array.Add(new SomeClass(i + 1));
            }

            // выводим инфу о них
            foreach (object item in array)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();

            // удаляем 3-й и 1-й
            array.RemoveAt(2);
            array.RemoveAt(0);

            // выводим инфу об оставшихся
            foreach (object item in array)
            {
                Console.WriteLine(item);
            }
        }
    }
}
#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

        string[] board = new string[8];
        for (int i = 0; i < 8; i++)
            board[i] = reader.ReadLine();

        int com = 0;
        (int x, int y) point = (0, 0);
        int remain = 0;
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                int myCom = 0;
                if (i > 0 && j > 0 && board[i - 1][j - 1] == 'O') myCom++;
                if (i > 0 && board[i - 1][j] == 'O') myCom++;
                if (j > 0 && board[i][j - 1] == 'O') myCom++;
                if (board[i][j] == 'O')
                {
                    myCom++;
                    remain++;
                }

                if (i > 0 && j > 0 && com < myCom)
                {
                    com = myCom;
                    point = (i, j);
                }
            }
        }

        writer.WriteLine(point.x + " " + point.y);

        int Choose(int n, int k) {
            int result = 1;
            for (int i = 1; i <= k; i++) {
                result = result * (n - k + i) / i;
            }
            return result;
        }

        double fail = (double)Choose(remain - com, 4) / Choose(remain, 4);
        writer.WriteLine($"{1 - fail:F10}");

        writer.Flush();
    }
}
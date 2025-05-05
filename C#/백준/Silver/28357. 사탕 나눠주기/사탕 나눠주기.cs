#nullable disable

partial class Program {
    public static void Main() {
        StreamReader reader = new StreamReader(Console.OpenStandardInput());
        StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());
        
        long[] NK = Array.ConvertAll(reader.ReadLine().Split(' '), long.Parse);
        long[] score = Array.ConvertAll(reader.ReadLine().Split(' '), long.Parse);
        
        bool simulate(long x) {
            long candy = NK[1];
            foreach (long sc in score) {
                candy -= Math.Max(0, sc - x);
                if (candy < 0) return false;
            }
            return true;
        }

        long start = 0, end = score.Max();
        while (start < end) {
            long mid = (start + end) / 2;
            if (simulate(mid)) {
                end = mid;
            }
            else {
                start = mid + 1;
            }
        }
        writer.WriteLine(end);
        
        writer.Flush();
    }
}
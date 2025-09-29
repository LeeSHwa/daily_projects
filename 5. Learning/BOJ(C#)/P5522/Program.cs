// https://www.acmicpc.net/problem/5522

// 문제 - 카드 게임

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program{
    static void Main(string[] args){
        List<int> scores = new List<int>();

        for (int i = 0; i < 5; i++){
            scores.Add(int.Parse(Console.ReadLine()));
        }

        Console.WriteLine(scores.Sum());
    }
}
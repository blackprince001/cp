fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();

    let input = input.trim().split_whitespace().collect::<Vec<&str>>();
    let n = input[0].parse::<usize>().unwrap();
    let k = input[1].parse::<usize>().unwrap();

    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    s = s.trim().to_string();

    let out = solve(&mut s, n, k);
    println!("{}", out);
}

fn solve(s: &mut String, n: usize, k: usize) -> String {
    let mut chars = s.chars().collect::<Vec<char>>();

    let mut i = 0;
    for _ in 0..k {
        while i < n - 1 {
            if chars[i] == 'B' && chars[i + 1] == 'G' {
                chars.swap(i, i + 1);
                i += 2;
            } else {
                i += 1;
            }
        }
        i = 0;
    }

    let out = chars.iter().collect::<String>();
    out
}

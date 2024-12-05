use std::{cmp::max, collections::HashMap, fs::File, hash::Hash, io::Read, path::Path};

fn main() {
    let input = read_file_to_string("input.txt");
    let mut pyramid = Pyramid::new(&input);
    let max_path = pyramid
        .max_path_from_memo(&Coordinate { y: 0, x: 0 })
        .unwrap_or(0);
    println!("max path: {}", max_path);
}

#[derive(Debug, Hash, Eq, PartialEq, Copy, Clone)]
struct Coordinate {
    y: i32,
    x: i32,
}

impl Coordinate {
    fn children(&self) -> (Coordinate, Coordinate) {
        (
            Coordinate {
                y: self.y + 1,
                x: self.x,
            },
            Coordinate {
                y: self.y + 1,
                x: self.x + 1,
            },
        )
    }
}

struct Pyramid {
    data: HashMap<Coordinate, i64>,
    max_path_lookup: HashMap<Coordinate, i64>,
}

impl Pyramid {
    fn new(input: &str) -> Self {
        let mut data = HashMap::new();
        for (y, line) in input.lines().enumerate() {
            for (x, number_str) in line.split(' ').enumerate() {
                let number: i64 = number_str.parse().unwrap();
                data.insert(
                    Coordinate {
                        x: x as i32,
                        y: y as i32,
                    },
                    number,
                );
            }
        }
        Self {
            data,
            max_path_lookup: HashMap::new(),
        }
    }

    fn print(&self) {
        println!("{:?}", self.data);
    }

    fn read_value(&self, coord: &Coordinate) -> Option<&i64> {
        self.data.get(coord)
    }

    fn max_path_from(&self, coord: &Coordinate) -> Option<i64> {
        let current = *self.read_value(coord)?;
        let (left_coord, right_coord) = coord.children();
        let left_path = self.max_path_from(&left_coord).unwrap_or(0);
        let right_path = self.max_path_from(&right_coord).unwrap_or(0);
        Some(max(left_path, right_path) + current)
    }

    fn max_path_from_memo(&mut self, coord: &Coordinate) -> Option<i64> {
        let memo = self.max_path_lookup.get(coord);
        if let Some(m) = memo {
            return Some(*m);
        }
        let current = *self.read_value(coord)?;
        let (left_coord, right_coord) = coord.children();
        let left_path = self.max_path_from_memo(&left_coord).unwrap_or(0);
        let right_path = self.max_path_from_memo(&right_coord).unwrap_or(0);
        let ret = max(left_path, right_path) + current;
        self.max_path_lookup.insert(*coord, ret);
        Some(ret)
    }
}

fn read_file_to_string(filename: &str) -> String {
    let path = Path::new(filename);
    let mut file = match File::open(path) {
        Err(why) => panic!("Couln't open {}: {}", path.display(), why),
        Ok(file) => file,
    };
    let mut s = String::new();
    file.read_to_string(&mut s).unwrap();
    s
}

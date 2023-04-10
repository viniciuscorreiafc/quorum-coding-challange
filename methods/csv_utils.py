import csv
from typing import TypeVar, Callable, Dict, List

T = TypeVar("T")

def read_csv(file_path: str, constructor: Callable[..., T]) -> List[T]:
  instances = []
  with open(file_path, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      instance = constructor(**row)
      instances.append(instance)
  return instances

def write_csv(file_name: str, data: List[Dict[str, str]]) -> None:
  with open(f"results/{file_name}", "w", newline="") as file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
      writer.writerow(row)
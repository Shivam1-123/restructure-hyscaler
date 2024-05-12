import csv

def last_slash(urls):
  # Split the URL by "/"
  parts = urls.split("/")

  # Join the first few parts to reconstruct the desired URL
  desired_url = "/".join(parts[:4])
  return desired_url

def process_csv(input_file, output_file):


  # Read the input CSV file
  with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    ld = list(reader)
    first_column_values = [sublist[0] for sublist in ld]

    column = last_elements = [url.split("/")[-1] for url in first_column_values]
    header = ["url"]
    for item in column:
      if item not in header:
        header.append(item)
  site = first_column_values[0].rsplit("/", 1)[0]

  count = len(header)
  i=0

  # Write the output CSV file
  with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    while i < len(first_column_values):
      list_ = [" "] * count
      n = first_column_values[i].rsplit("/", 1)[0]

      list_[0] = n
      while n == site:

        if i >= len(first_column_values):
          break
        else:
          index = header.index(column[i])
          list_[index] = ld[i][1]
          i += 1
          if i < len(first_column_values):
            site = first_column_values[i].rsplit("/", 1)[0]

      writer.writerow(list_)


if __name__ == "__main__":
  input_file = "input.csv"
  output_file = "output.csv"
  process_csv(input_file, output_file)

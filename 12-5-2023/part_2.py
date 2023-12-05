from part_1 import load_input, parse_input


temp_seeds, mappings = parse_input(load_input("input.txt"))
seeds = [(temp_seeds[i], temp_seeds[i] + temp_seeds[i + 1]) for i in range(0, len(temp_seeds) - 1, 2)]


def find_mappings(seeds, mappings):
    for intervals in mappings:
        new_seeds = []
        while seeds:
            start, end = seeds.pop()
            for start_desc, start_source, increment in intervals:
                overlap_start = start if start > start_source else start_source
                if end < start_source + increment:
                    overlap_end = end
                else:
                    overlap_end = start_source + increment
                if overlap_start < overlap_end:
                    new_seeds.append((overlap_start - start_source + start_desc, overlap_end - start_source + start_desc))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if overlap_end < end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new_seeds.append((start, end))
        seeds = new_seeds
    return seeds


def find_min_number(seeds):
    min_number = seeds[0][0]
    for seed, _ in seeds:
        if seed < min_number:
            min_number = seed
    return min_number


print(find_min_number(find_mappings(seeds, mappings)))

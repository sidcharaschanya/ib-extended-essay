import sys
import time
import random as rand
import csv
import quicksort as quick
import merge_sort as merge
import insertion_sort as ins

# Increasing recursion limit to allow quicksort to run with large data set sizes
sys.setrecursionlimit(10 ** 5)

# Initializing variables
properties = ["Random", "Few Unique", "Nearly Sorted"]
sizes = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
trials = 6
all_times = []
txt_file = open("eelists.txt", "w")

# Loop for each data set property
for i in range(len(properties)):
    # Initializing lists to store runtime for all data set sizes
    q_times = []
    m_times = []
    i_times = []

    # Loop for each data set size
    for j in range(len(sizes)):
        # Initializing lists to store trials for each data set size
        q_trials = [properties[i], "Quicksort", sizes[j]]
        m_trials = [properties[i], "Merge Sort", sizes[j]]
        i_trials = [properties[i], "Insertion Sort", sizes[j]]

        # Loop for each trial
        for k in range(trials):
            # Logging current trial
            print(f"{properties[i]}, {sizes[j]}, Trial #{k + 1}")

            # Initializing data set to be generated
            array = []

            # Generating completely random data set
            if i == 0:
                [array.append(rand.randint(1, sizes[j] * 100)) for _ in range(sizes[j])]

            # Generating data set containing few unique values
            if i == 1:
                values = [rand.randint(1, sizes[j]) for _ in range(sizes[j] // 100)]
                [array.append(values[rand.randint(0, sizes[j] // 100 - 1)]) for _ in range(sizes[j])]

            # Generating nearly sorted data set
            if i == 2:
                array.extend(range(1, sizes[j]))
                array.insert(rand.randint(1, sizes[j] - 2), sizes[j])

            # Writing generated data set to text file
            txt_file.write(f"{properties[i]}, {sizes[j]}, Trial #{k + 1}\n{array}\n\n")

            # Executing sorting algorithms with each trial having a different permutation
            if k == 0:
                one = time.time()
                quick.quicksort(array.copy(), 0, len(array) - 1)
                two = time.time()
                merge.merge_sort(array.copy())
                three = time.time()
                ins.insertion_sort(array.copy())
                four = time.time()
                q_trials.append(two - one)
                m_trials.append(three - two)
                i_trials.append(four - three)
            if k == 1:
                one = time.time()
                quick.quicksort(array.copy(), 0, len(array) - 1)
                two = time.time()
                ins.insertion_sort(array.copy())
                three = time.time()
                merge.merge_sort(array.copy())
                four = time.time()
                q_trials.append(two - one)
                i_trials.append(three - two)
                m_trials.append(four - three)
            if k == 2:
                one = time.time()
                merge.merge_sort(array.copy())
                two = time.time()
                quick.quicksort(array.copy(), 0, len(array) - 1)
                three = time.time()
                ins.insertion_sort(array.copy())
                four = time.time()
                m_trials.append(two - one)
                q_trials.append(three - two)
                i_trials.append(four - three)
            if k == 3:
                one = time.time()
                merge.merge_sort(array.copy())
                two = time.time()
                ins.insertion_sort(array.copy())
                three = time.time()
                quick.quicksort(array.copy(), 0, len(array) - 1)
                four = time.time()
                m_trials.append(two - one)
                i_trials.append(three - two)
                q_trials.append(four - three)
            if k == 4:
                one = time.time()
                ins.insertion_sort(array.copy())
                two = time.time()
                quick.quicksort(array.copy(), 0, len(array) - 1)
                three = time.time()
                merge.merge_sort(array.copy())
                four = time.time()
                i_trials.append(two - one)
                q_trials.append(three - two)
                m_trials.append(four - three)
            if k == 5:
                one = time.time()
                ins.insertion_sort(array.copy())
                two = time.time()
                merge.merge_sort(array.copy())
                three = time.time()
                quick.quicksort(array.copy(), 0, len(array) - 1)
                four = time.time()
                i_trials.append(two - one)
                m_trials.append(three - two)
                q_trials.append(four - three)

        # Copying list of trials into respective list of times
        q_times.append(q_trials)
        m_times.append(m_trials)
        i_times.append(i_trials)

    # Copying each list of times into list storing all times
    all_times.extend(q_times)
    all_times.extend(m_times)
    all_times.extend(i_times)

txt_file.close()

# Writing all times to csv file
with open("eedata.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([
        "Data Set Property", "Sorting Algorithm", "Number Of Elements",
        "Trial #1", "Trial #2", "Trial #3", "Trial #4", "Trial #5", "Trial #6"
    ])
    csv_writer.writerows(all_times)

# Logging completion
print("Done")

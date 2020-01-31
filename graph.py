import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def graph_bench(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bench")

    rows = cur.fetchall()

    workouts = []
    weights = []

    for row in rows:
        workouts.append(row[0])
        weights.append(row[2])

    plt.plot(workouts, weights, '-')
    plt.xlabel('Workout Number')
    plt.ylabel('Weight Benched')
    plt.show()

def main():
    conn = sqlite3.connect("workouts.db")

    graph_bench(conn)

if __name__ == "__main__":
    main()

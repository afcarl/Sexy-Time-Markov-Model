Sexy-Time-Markov-Model
======================

A Markov model for simulating sex!

<p><b>Step 1.</b></p>

Download the ZIP (to the right) containing all of the files found in the GitHub repository.

<p><b>Step 2.</b></p>

Extract the ZIP.

<p><b>Step 3.</b></p>

Using a terminal, <code>cd</code> to the directory containing the files.

<p><b>Step 4.</b></p>

From the terminal, run:

<code>python sexy_time_markov_model.py "initial_probs.csv" "transition_probs.csv" "arousal_rates.csv" "time_parameters.csv"</code>

<p> All of the parameters contained in the CSV files can be tuned by the user, including the addition and removal of positions. The values in "initial_probs.csv" are used to determine (probabilistically) the starting position for the sex simulation. The values in "transition_probs.csv" are used to determine (probabilistically) the position changes during the sex simulation. The values in "arousal_rates.csv" are used to modify the arousal level of each partner during the sex simulation (they can also be thought of as "orgasms per second" parameters for each partner/position combination). Finally, the values in "time_parameters.csv" are used to determine the amount of time spent in each position during the sex simulation (as drawn from a gamma distribution).</p>

<p> The output is a list of positions followed by a summary line. Each line corresponding to a position includes the time spent in the position and the number of "orgasms" each partner has accumulated thus far in the simulation.</p>

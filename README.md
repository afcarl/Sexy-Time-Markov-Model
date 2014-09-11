Sexy-Time-Markov-Model
======================

A Markov model for sex!

<p><b>To run:</b><p>
<p>1. Download the .zip (to the right) containing all of the files found in the GitHub repository.</p>
<p>2. Extract the .zip.
<p>3. Using a terminal, cd to the directory containing the files.</p>
<p>4. run:</p>
<p>python sexyTimeMarkovModel.py "initialProbs.csv" "transitionProbs.csv" "arousalRates.csv" "timeParameters.csv"</p>

<p> All of the parameters contained in the .csv files can be tuned by the user, including the addition and removal of positions. The values in "initialProbs.csv" are used to determine (probabilistically) the starting position for the sex simulation. The values in "transitionProbs.csv" are used to determine (probabailistically) the position changes during the sex simulation. The values in "arousalRates.csv" are used to modify the arousal level of each partner during the sex simulation (they can also be thought of as "orgasms per second"). Finally, the values in "timeParameters.csv" are used to determine the amount of time spent in each position during the sex simulation (as drawn from a normal distribution).</p>

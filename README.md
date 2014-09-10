Sexy-Time-Markov-Model
======================

A Markov model for sex!

<p><b>To run:</b><p>
<p>1. Download the .zip (to the right) containing all of the files found in the GitHub repository.</p>
<p>2. Extract the .zip.
<p>3. Using a terminal, cd to the directory containing the files.</p>
<p>4. run:</p>
<p>python sexyTimeMarkovModel.py "initialProbs.csv" "transitionProbs.csv" "arousalRates.csv" "timeParameters.csv"</p>

<p> All of the parameters contained in the .csv files can be tuned by the user, including the addition and removal of positions. "initialProbs.csv" contains the probabilities of sex starting in different positions. "transitionProbs.csv" provides the probabilities of changing from one position to another. "arousalRates.csv" is used to indicate how stimulating a given position is for each partner (it can also be thought of as "orgasms per second"). Finally, "timeParameters.csv" provides the parameters that are used to determine the amount of time spent in each position during sex (as drawn from a normal distribution).</p>

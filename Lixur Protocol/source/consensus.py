'''
Lixur uses a new consensus mechanism called Enchanted Consensus, which is a modified version of the Avalanche consensus but slush querying is weighted.
The weight makes it so that nodes with higher influence are more likely to be queried for their opinion.
The weight is designed in a way so that an attacker would have to have most the following to influence the consensus to it's benefit:
1. Be an old account, preferably one of the oldest accounts on the network
2. Have a significant percentage of the total supply
3. Have validated/made a large number of transactions (making it do a considerable amount of work)
4. The total cumulative weight of all transactions it has validated would have to be a significant fraction of the total weight of all transactions in the network.
5. Have a significant amount of the computational power of the network.
This is impossible to achieve. Way, way, way too much money, work, power and time needed and that's just to get a chance of influencing the consensus.
It is nearly impossible for a byzantine node to influence the consensus.
With Enchanted Consensus, a prerequisite for a byzantine to maliciously influence the consensus is that it would have to be god on the network.
'''
from numpy.random import default_rng
from numpy import abs, array, zeros
import time
from typing import Tuple, TextIO
import argparse
import json
import numpy
import sys
# TODO: Add a way to specify the number of active nodes in the network
# TODO: Add a way to specify the number of byzantines in the network
# TODO: Add a way to associate nodes with their influence scores
# TODO: Add a way to properly add the weights of each node to the slush part
# TODO: Fix the weight function and node influence part and the on the __main__ section

# Turn this into a single function and also run it through a JIT compiler
'''
import time
time_of_creation = time.time() # The time of creation of a wallet should be added to the graph, and can be referenced whenever.
def node_influence():
    def account_age():
        if time.time() - time_of_creation < 2.628e+6:  # If account is younger than a month
            age = 0
        elif time.time() - time_of_creation >= 2.628e+6 and time.time() - time_of_creation < 1.577e+7:  # If account is a month to six months old
            age = 1
        elif time.time() - time_of_creation >= 1.577e+7 and time.time() - time_of_creation < 3.154e+7:  # If account is six months to a year old
            age = 2
        elif time.time() - time_of_creation >= 3.154e+7 and time.time() - time_of_creation < 9.461e+7:  # If account is a year to three years old
            age = 3
        elif time.time() - time_of_creation >= 9.461e+7 and time.time() - time_of_creation < 1.577e+8:  # If account is three years to five years old
            age = 4
        elif time.time() - time_of_creation >= 1.577e+8 and time.time() - time_of_creation < 3.154e+8:  # If account is five years to ten years old
            age = 5
        elif time.time() - time_of_creation >= 3.154e+8 and time.time() - time_of_creation < 1.577e+9:  # If account is ten years to fifty years old
            age = 6
        elif time.time() - time_of_creation >= 1.577e+9 and time.time() - time_of_creation < 3.154e+9:  # If account is fifty years to a hundred years old
            age = 7
        elif time.time() - time_of_creation >= 3.154e+9 and time.time() - time_of_creation < 3.154e+10:  # If account is a hundred years to a thousand years old
            age = 8
        elif time.time() - time_of_creation >= 3.154e+10 and time.time() - time_of_creation < 3.1536e+11:  # If account is a thousand years to nine thousand years old
            age = 9
        elif time.time() - time_of_creation >= 2.8382e+11:  # If account is over 9000!!!
            age = 10
        return age
    def account_activity(tx_count):
        if tx_count < 100:  # If account is younger than a month
            activity = 0
        elif tx_count >= 100 and tx_count < 1000:  # If account is a month to six months old
            activity = 1
        elif tx_count >= 1000 and tx_count < 10000:  # If account is six months to a year old
            activity = 2
        elif tx_count >= 10000 and tx_count < 100000:  # If account is a year to three years old
            activity = 3
        elif tx_count >= 100000 and tx_count < 1000000:  # If account is three years to five years old
            activity = 4
        elif tx_count >= 1000000 and tx_count < 10000000:  # If account is five years to ten years old
            activity = 5
        elif tx_count >= 10000000 and tx_count < 100000000:  # If account is ten years to fifty years old
            activity = 6
        elif tx_count >= 100000000 and tx_count < 1000000000:
            activity = 7
        elif tx_count >= 1000000000 and tx_count < 10000000000:
            activity = 8
        elif tx_count >= 10000000000 and tx_count < 100000000000:
            activity = 9
        elif tx_count >= 100000000000:
            activity = 10
        return activity
    def compute_power():
        import time
        import platform
        import cpuinfo  # install CPU Info package (pip install py-cpuinfo)

        start_benchmark = 10  # change this if you like (sample: 1000, 5000, etc)
        start_benchmark = int(start_benchmark)

        repeat_benchmark = 1  # attemps, change this if you like (sample: 3, 5, etc)
        repeat_benchmark = int(repeat_benchmark)

        average_benchmark = 0

        for a in range(0, repeat_benchmark):

            start = time.time()

            for i in range(0, start_benchmark):
                for x in range(1, 1000):
                    3.141592 * 2 ** x
                for x in range(1, 10000):
                    float(x) / 3.141592
                for x in range(1, 10000):
                    float(3.141592) / x

            end = time.time()
            duration = (end - start)
            duration = round(duration, 3)
            average_benchmark += duration

        average_benchmark = round(average_benchmark / repeat_benchmark, 3)
        score = (0.5 * start_benchmark) - average_benchmark
        return score
    def balance_of_node(balance):
        fin_influence = (balance / 69420000) * 100
        return fin_influence
    def cumulative_weight(cumulative_weight):
        if cumulative_weight < 10:
            weight = 0
        elif cumulative_weight >= 10 and cumulative_weight < 100:
            weight = 1
        elif cumulative_weight >= 100 and cumulative_weight < 1000:
            weight = 2
        elif cumulative_weight >= 1000 and cumulative_weight < 10000:
            weight = 3
        elif cumulative_weight >= 10000 and cumulative_weight < 100000:
            weight = 4
        elif cumulative_weight >= 100000 and cumulative_weight < 1000000:
            weight = 5
        elif cumulative_weight >= 1000000 and cumulative_weight < 10000000:
            weight = 6
        elif cumulative_weight >= 10000000 and cumulative_weight < 100000000:
            weight = 7
        elif cumulative_weight >= 100000000 and cumulative_weight < 1000000000:
            weight = 8
        elif cumulative_weight >= 1000000000 and cumulative_weight < 10000000000:
            weight = 9
        elif cumulative_weight >= 10000000000:
            weight = 10
        return weight
    def calculate_score():
        x = ({'age': account_age(), 'transactions': account_activity(0), 'computing_power': compute_power(),
              'financial_influence': balance_of_node(0), 'cumulative_weight': cumulative_weight(0)})
        influence = (x['age'] + x['transactions'] + x['computing_power'] + x['financial_influence'] + x['cumulative_weight']) * 2 / 5
        print(f'Your node influence score is: {round(influence, 2)}/100')
    calculate_score()
node_influence = node_influence()
'''
# Essentially you would need to be able to have nodes query each other for their opinion
# You would need to have slush work in a real setting, meaning these nodes would have to return an opinion
# Other nodes will assimilate
# The likelihood of a node getting queried for its opinion is proportional to its influence
# And the byzantine's opinion should get weeded each round.

def avalanche(population_weights: array, max_round: int, max_sample: int, min_sample: int, quorum_rate: float, byzantine_rate: float) -> array:
    """
    Simulates for the provided number of `max_round`, the given
    `population_weights.size` and `max_sample` an **Avalanche** process,
    where *all* sample sizes in the [`min_sample`,`max_sample`]
    range are simulated for! Then, a matrix for *each* round &&
    sample size is returned.
    The `byzantine_rate` is the **percentage** of population, which is
    malicious towards the network attempting to flip peer nodes
    w/o actually following the consensus rules.
    """
    m = zeros(shape=(max_round, max_sample))
    for x in range(min_sample, max_sample + 1):

        p = population(population_weights.size)
        c = counters(population_weights.size)
        for z in range(max_round):
            p += errors(population_weights, byzantine_rate)
            p %= 2
            m[z, x - 1] = numpy.sum(population_weights * p)
            p = snowflake(*slush(p, population_weights, x, quorum_rate), c)

    return m
def population(population_size: int) -> array:
    """
    Returns a *uniformly* sampled population for given `population_size`
    where a value of `0` represents *yellow* and a value of `1`
    *red* cards.
    """
    return prg.integers(0, 2, size=population_size)
def counters(population_size: int) -> array:
    """
    Returns a zero-initialized array of conviction counters for
    the given population size (of `population_size`).
    """
    return zeros(population_size, dtype=numpy.int64)
def errors(node_influence: array, byzantine_rate=0.0) -> array:
    """
    Returns a stake-weighted population of adversarial members,
    with `byzantine_rate` being the *percentage* of the total weights.
    """
    return node_influence.cumsum() < byzantine_rate
def slush(population: array, node_influence: array, size: int, quorum_rate: float) -> array:
    """
    Applies the stake-weighted Slush polling mechanism for `population`:
    Make a random choice of a sample `size` (from a given array
    `population`) for *each* element within the array `population`.
    Then for each sample, determine if the α-majority of the sample indicates
    *red* (i.e. `1`) or *yellow* (i.e. `0`) cards.  However if
    there is *no* α-majority (i.e. tie) within the sample, then
    do nothing.
    """
    ps = prg.choice(population, size=(size, population.size),p=node_influence).sum(axis=0)
    eq, gt = ps == (1 - quorum_rate) * size, ps > (1 - quorum_rate) * size

    return population * eq + gt, population, gt
def snowflake(n: array, p: array, gt: array, c: array) -> array:
    """
    Applies the Snowflake conviction model onto the population.
    """
    lt, gte = c < args.beta_1, c >= args.beta_1
    c += lt * (n == p) + gte * 0  ## color' == color => c[i]+= 1
    c *= lt * (n == p) + gte * 1  ## color' != color => c[i] = 0
    c += lt * (n != p) + gte * 0  ## color' != color => c[i] = 1
    c *= lt * (gt > 0) + gte * 1  ## *no* α-majority => c[i] = 0

    if args.debug_level > 0:
        print(p, file=sys.stderr)
    if args.debug_level > 1:
        print(n, file=sys.stderr)
    if args.debug_level > 2:
        print(c, file=sys.stderr)

    return (c < args.beta_1) * n + (c >= args.beta_1) * p
def weights(population_size: int, distribution: str, exponent: float) -> array:
    """
    Returns various weight distributions (ie validator stakes).
    """
    def norm(node_influence):
        node_influence_exp = numpy.power(node_influence, exponent)
        return numpy.sort(node_influence_exp) / node_influence_exp.sum()

    if distribution == 'cauchy':
        return norm(abs(prg.standard_cauchy(population_size)))
    elif distribution == 'equal':
        return norm(numpy.ones(population_size))
    elif distribution == 'exponential':
        return norm(prg.standard_exponential(population_size))
    elif distribution == 'gamma':
        _, shape = distribution.split('-')
        return norm(prg.standard_gamma(float(shape), population_size))
    elif distribution == 'normal':
        return norm(abs(prg.standard_normal(population_size)))
    elif distribution.startswith('pareto'):
        _, alpha = distribution.split('-')
        return norm(prg.pareto(float(alpha), population_size))
    elif distribution == 'total-weights':
        return norm(load(sys.stdin)[1])
    elif distribution == 'weights':
        return norm(load(sys.stdin)[0])
    else:
        return norm(prg.uniform(0, 1.0, population_size))
def load(file: TextIO) -> Tuple[array, array]:
    """
    Validator weights & total weights (i.e. w/[o] delegations).
    """
    node_influence = []  ## validator weight excl. delegations
    total_influence = []  ## validator weight incl. delegations

    for line in file.readlines():
        validators = json.loads(line)
        validators = validators['data']
        validators = validators['validators']
        validators = validators['results']

        node_influence.extend(map(lambda v: v['weight'], validators))
        total_influence.extend(map(lambda v: v['totalWeight'], validators))

    return array(node_influence), array(total_influence)
if __name__ == '__main__':
    start_time = time.time()
    parser = argparse.ArgumentParser(description='Produces the Avalanche simulation matrix ''[max_round x max_sample]')
    parser.add_argument('-p', '--population', type=int, help='population size''(default: %(default)s)', default=2)
    parser.add_argument('-d', '--distribution', choices=['cauchy', 'equal', 'exponential', 'normal', 'uniform',
    'pareto-3', 'pareto-2', 'pareto-1', 'pareto-0.5','gamma-3', 'gamma-2', 'gamma-1', 'gamma-0.5', 'total-weights', 'weights'], # i.e. stdin
    type=str, help='stake distribution'' (default: %(default)s)', default='uniform')
    parser.add_argument('-x', '--distribution-exponent', type=float, help='stake distribution exponent'' (default: %(default)s)', default=1.0)
    parser.add_argument('-R', '--max-round',type=int, help='maximum number of rounds'' (default: %(default)s)', default=25)
    parser.add_argument('-s', '--min-sample',type=int, help='minimum sample size '' (default: %(default)s)', default=1)
    parser.add_argument('-S', '--max-sample',type=int, help='maximum sample size '' (default: %(default)s)', default=25)
    parser.add_argument('-q', '--quorum-rate',type=float, help='quorum rate in [0.0, 1.0]'' (default: %(default)s)', default=0.69)
    parser.add_argument('-b1', '--beta-1', type=int, help='virtuous commit threshold '' (default: %(default)s)', default=15)
    parser.add_argument('-e', '--error-share', type=float, help='error share in [0.0, 0.5]'' (default: %(default)s)', default=0.10)
    parser.add_argument('--random-seed',type=int, help='random generator seed'' (default: %(default)s)', default=None)
    parser.add_argument('--debug-level',type=int, choices=[0, 1, 2, 3], help='debug level'' (default: %(default)s)', default=0)
    args = parser.parse_args()
    prg = default_rng(args.random_seed)

    node_influence = weights(args.population,args.distribution,args.distribution_exponent)
    m = avalanche(node_influence, args.max_round,args.max_sample, args.min_sample,args.quorum_rate, args.error_share)

    args = vars(args)
    args['population'] = node_influence.size
    numpy.savetxt(sys.stdout, m, header=json.dumps(args))
    end_time = time.time()
    print(f'Consensus achieved in {end_time - start_time} seconds')
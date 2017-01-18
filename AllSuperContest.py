import numpy as np
from scipy import stats
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


class AllSuperContest(object):

    def SimulateYear(self,entries,trials):
        push = 0.028
        win = (1.0-push)/2.
        pvals = [push,win,win]
        results = []
        mean_contest = []
        for _ in range(trials):
            games = np.random.multinomial(1,pvals,[17,15])
            contest = []
            for _ in range(entries):
                user_sum = 0.0
                bets = 0
                for w in games:
                #got one week, shuffle randomly
                    np.random.shuffle(w)
                    for g in w[0:5]:
                        if g[0] == 1:
                            user_sum += 0.5
                            continue
                        if np.random.rand() < 0.5:
                            user_sum += g[1]
                        else:
                            user_sum += g[2]
                contest.append(user_sum)
            mean_contest.append(np.mean(np.array(contest)))
            results.append(max(contest))
        print np.mean(mean_contest)
        return results



    def make_histogram(self,results):
    # the histogram of the data
        n, bins, patches = plt.hist(results, 41, range=[44.75,65.25], normed=1, facecolor='green', histtype='stepfilled',label='1854 Entry Simulation')
        vline = plt.axvline(55.5, color='b', linestyle='dashed', linewidth=2,label='2016 Winner')
        plt.xlabel('Winner Points')
        plt.ylabel('Probability')
        plt.title(r'Expected SuperContest Winner Points for Efficient Market')
        plt.axis([44.75, 65.25, 0, 0.4])
        plt.grid(True)
        plt.legend(handles=[vline])

        plt.show()

def main():
    print 'running'
    sc = AllSuperContest()
    history = [
    [1854,55.5],
    [1727,60.5],
    [1403,64.5],
    [1854,55.5],
    [1034,57],
    [745,57.5],
    [517,60.5],
    [345,55.5],
    [328,54.5],
    [350,56.5],
    [342,55.0],
    [416,57.5],
    [505,59],
    [411,52.5]
    ]

    pvalues = []
    for i in history:
        entries = i[0]
        results = sc.SimulateYear(entries,100)
        results.sort(reverse=True)
        p = 0
        for r in results:
            if r>i[1]:
                p=p+1
            else:
                break
        pvalue = float(p)/float(len(results))
        pvalues.append(pvalue)
    print pvalues
# do K-S test
    print stats.kstest(pvalues, 'uniform', args=(0,1))


if __name__ == '__main__':
    main()


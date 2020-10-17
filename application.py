import analysis

from argparse import ArgumentParser


def build_argparser():
    """
    Parse command line arguments.
    :return: command line arguments
    """
    parser = ArgumentParser()
    parser.add_argument("-q", "--query", required=True, type=str,
                        help="Search Query on Twitter")

    return parser


def main():
    """
    Load the network and parse the output.
    :return: None
    """
    # We get arguments from the command line:
    args = build_argparser().parse_args()

    # We carry out the analysis:
    final_score, lista_tweets = analisis.analyze_tweets(
        args.query, total_tweets=10)

    for tweet in lista_tweets:
        print(tweet)

    print("Final Score: ", final_score)


if __name__ == '__main__':
    main()

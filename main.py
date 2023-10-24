from scrape_forum import ScrapeForum


def main():
    sf = ScrapeForum(max_pages=2)
    sf.run()


if __name__ == '__main__':
    main()

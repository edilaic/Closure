TESTDIR=test
CASES=$(TESTDIR)/cases
WORK=$(TESTDIR)/work

all:
	find $(WORK) -exec chmod u+w {} + || true
	find $(WORK) -depth -delete || true
	mkdir -p $(WORK)
	rsync -a $(CASES)/ $(WORK)/
	find $(WORK)

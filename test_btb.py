# import sys
from filecmp import cmp
from pathlib import Path

import pytest

# TODO consider refactoring to simplify the import
# Modify the path because of the - in the directory
# SPRAS_ROOT = Path(__file__).parent.parent.parent.absolute()
# sys.path.append(str(Path(SPRAS_ROOT, 'docker-wrappers', 'LocalNeighborhood')))
from btb import btb_wrapper

TEST_DIR = Path('test')
OUT_FILE = Path(TEST_DIR, 'output', 'output.txt')
BTB_OUT_FILE = Path(TEST_DIR, 'output', 'btb-output.txt')
DISJOINT_OUT_FILE = Path(TEST_DIR, 'output', 'disjoint-output.txt')
DISJOINT2_OUT_FILE = Path(TEST_DIR, 'output', 'disjoint2-output.txt')


class TestBowTieBuilder:
    """
    Run the BowTieBuilder algorithm on the example input files and check the output matches the expected output
    """
    def test_btb(self):
        BTB_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(network_file=Path(TEST_DIR, 'input', 'btb-edges.txt'),
                           source_file=Path(TEST_DIR, 'input', 'btb-sources.txt'),
                           target_file=Path(TEST_DIR, 'input', 'btb-targets.txt'),
                           output_file=BTB_OUT_FILE)
        assert BTB_OUT_FILE.exists(), 'Output file was not written'
        expected_file = Path(TEST_DIR, 'expected_output', 'btb-output.txt')

        # Read the content of the output files and expected file into sets
        with open(BTB_OUT_FILE, 'r') as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, 'r') as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, 'Output file does not match expected output file'

    """
    Run the BowTieBuilder algorithm on the example disjoint input files and check the output matches the expected output
    """
    def test_disjoint(self):
        DISJOINT_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(network_file=Path(TEST_DIR, 'input', 'disjoint-edges.txt'),
                           source_file=Path(TEST_DIR, 'input', 'disjoint-sources.txt'),
                           target_file=Path(TEST_DIR, 'input', 'disjoint-targets.txt'),
                           output_file=DISJOINT_OUT_FILE)
        assert DISJOINT_OUT_FILE.exists(), 'Output file was not written'
        expected_file = Path(TEST_DIR, 'expected_output', 'disjoint-output.txt')

        # Read the content of the output files and expected file into sets
        with open(DISJOINT_OUT_FILE, 'r') as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, 'r') as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, 'Output file does not match expected output file'

    """
    Run the BowTieBuilder algorithm on the example disjoint2 input files and check the output matches the expected output
    """
    def test_disjoint2(self):
        DISJOINT2_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(network_file=Path(TEST_DIR, 'input', 'disjoint2-edges.txt'),
                           source_file=Path(TEST_DIR, 'input', 'disjoint-sources.txt'),
                           target_file=Path(TEST_DIR, 'input', 'disjoint-targets.txt'),
                           output_file=DISJOINT2_OUT_FILE)
        assert DISJOINT2_OUT_FILE.exists(), 'Output file was not written'
        expected_file = Path(TEST_DIR, 'expected_output', 'disjoint-output.txt')
        
        # Read the content of the output files and expected file into sets
        with open(DISJOINT2_OUT_FILE, 'r') as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, 'r') as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, 'Output file does not match expected output file'

    """
    Run the BowTieBuilder algorithm with a missing input file
    """
    def test_missing_file(self):
        with pytest.raises(OSError):
            btb_wrapper(network_file=Path(TEST_DIR, 'input', 'missing.txt'),
                           source_file=Path(TEST_DIR, 'input', 'btb-sources.txt'),
                           target_file=Path(TEST_DIR, 'input', 'btb-targets.txt'),
                           output_file=OUT_FILE)

    # """
    # Run the BowTieBuilder algorithm with an improperly formatted network file
    # """
    # def test_format_error(self):
    #     with pytest.raises(ValueError):
    #         btb_wrapper(edge_file=Path(TEST_DIR, 'input', 'btb-bad-edges.txt'),
    #                         source_file=Path(TEST_DIR, 'input', 'btb-sources.txt'),
    #                         target_file=Path(TEST_DIR, 'input', 'btb-targets.txt'),
    #                         output_file=OUT_FILE)

    # Write tests for the BowTieBuilder run function here
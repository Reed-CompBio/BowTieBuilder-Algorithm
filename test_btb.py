# import sys
from filecmp import cmp
from pathlib import Path

import pytest

# TODO consider refactoring to simplify the import
# Modify the path because of the - in the directory
from btb import btb_wrapper

TEST_DIR = Path("test")
OUT_FILE = Path(TEST_DIR, "output", "output.txt")
BTB_OUT_FILE = Path(TEST_DIR, "output", "btb-output.txt")
DISJOINT_OUT_FILE = Path(TEST_DIR, "output", "disjoint-output.txt")
DISJOINT2_OUT_FILE = Path(TEST_DIR, "output", "disjoint2-output.txt")
SOURCE_TO_SOURCE_OUT_FILE = Path(TEST_DIR, "output", "source-to-source-output.txt")
SOURCE_TO_SOURCE2_OUT_FILE = Path(TEST_DIR, "output", "source-to-source2-output.txt")
SOURCE_TO_SOURCE_DISJOINT_OUT_FILE = Path(
    TEST_DIR, "output", "source-to-source-disjoint-output.txt"
)
BIDIRECTIONAL_OUT_FILE = Path(TEST_DIR, "output", "bidirectional-output.txt")
TARGET_TO_SOURCE_OUT_FILE = Path(TEST_DIR, "output", "target-to-source-output.txt")
LOOP_OUT_FILE = Path(TEST_DIR, "output", "loop-output.txt")
WEIGHTED_OUT_FILE = Path(TEST_DIR, "output", "weighted-output.txt")
NO_WEIGHT_OUT_FILE = Path(TEST_DIR, "output", "no-weight-output.txt")
WEIGHT_ONE_OUT_FILE = Path(TEST_DIR, "output", "weight-one-output.txt")


class TestBowTieBuilder:
    """
    Run the BowTieBuilder algorithm on the example input files and check the output matches the expected output
    """

    def test_btb(self):
        BTB_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "btb-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=BTB_OUT_FILE,
        )
        assert BTB_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "btb-output.txt")

        # Read the content of the output files and expected file into sets
        with open(BTB_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the example disjoint input files and check the output matches the expected output
    """

    def test_disjoint(self):
        DISJOINT_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "disjoint-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "disjoint-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "disjoint-targets.txt"),
            output_file=DISJOINT_OUT_FILE,
        )
        assert DISJOINT_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "disjoint-output.txt")

        # Read the content of the output files and expected file into sets
        with open(DISJOINT_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the example disjoint2 input files and check the output matches the expected output
    """

    def test_disjoint2(self):
        DISJOINT2_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "disjoint2-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "disjoint-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "disjoint-targets.txt"),
            output_file=DISJOINT2_OUT_FILE,
        )
        assert DISJOINT2_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "disjoint-output.txt")

        # Read the content of the output files and expected file into sets
        with open(DISJOINT2_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm with a missing input file
    """

    def test_missing_file(self):
        with pytest.raises(OSError):
            btb_wrapper(
                edges=Path(TEST_DIR, "input", "missing.txt"),
                sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
                targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
                output_file=OUT_FILE,
            )

    """
    Run the BowTieBuilder algorithm on the example source to source input files and check the output matches the expected output
    """

    def test_source_to_source(self):
        SOURCE_TO_SOURCE_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "source-to-source-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=SOURCE_TO_SOURCE_OUT_FILE,
        )
        assert SOURCE_TO_SOURCE_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "source-to-source-output.txt")

        # Read the content of the output files and expected file into sets
        with open(SOURCE_TO_SOURCE_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the example source to source input files and check the output matches the expected output
    """

    def test_source_to_source2(self):
        SOURCE_TO_SOURCE2_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "source-to-source2-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=SOURCE_TO_SOURCE2_OUT_FILE,
        )
        assert SOURCE_TO_SOURCE2_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(
            TEST_DIR, "expected_output", "source-to-source2-output.txt"
        )

        # Read the content of the output files and expected file into sets
        with open(SOURCE_TO_SOURCE2_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on two separate source to target paths connected by sources and check the output matches the expected output
    """

    def test_source_to_source_disjoint(self):
        SOURCE_TO_SOURCE_DISJOINT_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "source-to-source-disjoint-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=SOURCE_TO_SOURCE_DISJOINT_OUT_FILE,
        )
        assert SOURCE_TO_SOURCE_DISJOINT_OUT_FILE.exists(), (
            "Output file was not written"
        )
        expected_file = Path(
            TEST_DIR, "expected_output", "source-to-source-disjoint-output.txt"
        )

        # Read the content of the output files and expected file into sets
        with open(SOURCE_TO_SOURCE_DISJOINT_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the example bidirectional input files and check the output matches the expected output
    """

    def test_bidirectional(self):
        BIDIRECTIONAL_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "bidirectional-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=BIDIRECTIONAL_OUT_FILE,
        )
        assert BIDIRECTIONAL_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "bidirectional-output.txt")

        # Read the content of the output files and expected file into sets
        with open(BIDIRECTIONAL_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the example target to source input files and check the output matches the expected output
    """

    def test_target_to_source(self):
        TARGET_TO_SOURCE_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "target-to-source-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=TARGET_TO_SOURCE_OUT_FILE,
        )
        assert TARGET_TO_SOURCE_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "empty-output.txt")

        # Read the content of the output files and expected file into sets
        with open(TARGET_TO_SOURCE_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the example loop network files and check the output matches the expected output
    """

    def test_loop(self):
        LOOP_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "loop-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=LOOP_OUT_FILE,
        )
        assert LOOP_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "loop-output.txt")

        # Read the content of the output files and expected file into sets
        with open(LOOP_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    """
    Run the BowTieBuilder algorithm on the weighted input files and check the output matches the expected output
    """

    def test_weighted(self):
        WEIGHTED_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "weighted-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=WEIGHTED_OUT_FILE,
        )
        assert WEIGHTED_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "weighted-output.txt")

        # Read the content of the output files and expected file into sets
        with open(WEIGHTED_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    def test_no_weight(self):
        NO_WEIGHT_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "no-weight-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=NO_WEIGHT_OUT_FILE,
        )
        assert NO_WEIGHT_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "weighted-output.txt")

        # Read the content of the output files and expected file into sets
        with open(NO_WEIGHT_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

    def test_weight_one(self):
        WEIGHT_ONE_OUT_FILE.unlink(missing_ok=True)
        btb_wrapper(
            edges=Path(TEST_DIR, "input", "weight-one-edges.txt"),
            sources_path=Path(TEST_DIR, "input", "btb-sources.txt"),
            targets_path=Path(TEST_DIR, "input", "btb-targets.txt"),
            output_file=WEIGHT_ONE_OUT_FILE,
        )
        assert WEIGHT_ONE_OUT_FILE.exists(), "Output file was not written"
        expected_file = Path(TEST_DIR, "expected_output", "weighted-output.txt")

        # Read the content of the output files and expected file into sets
        with open(WEIGHT_ONE_OUT_FILE, "r") as output_file:
            output_content = set(output_file.read().splitlines())
        with open(expected_file, "r") as expected_output_file:
            expected_content = set(expected_output_file.read().splitlines())

        # Check if the sets are equal, regardless of the order of lines
        assert output_content == expected_content, (
            "Output file does not match expected output file"
        )

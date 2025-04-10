import click
from benchmark import CIFixBenchmark
from benhmark_functions import fix_apply_diff, fix_none

@click.command()
@click.option('--model-name', required=True, help='Name of the model')
@click.option('--config-path', required=True, help='Path to the configuration file')
@click.option('--result-filename', required=True, help='Filename to store the results')
@click.option('--job-ids-file', required=True, help='Path to the job IDs file')
def run_benchmark(model_name, config_path, result_filename, job_ids_file):
    """Run the CIFixBenchmark with the specified parameters."""
    CIBenchPython = CIFixBenchmark(model_name, config_path)
    job_results = CIBenchPython.eval_jobs(job_ids_file=job_ids_file, result_filename=result_filename)
    click.echo(f"Benchmark completed. Results saved to {result_filename}")

if __name__ == '__main__':
    run_benchmark()

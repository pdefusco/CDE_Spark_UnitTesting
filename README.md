# Spark Unit Testing in CDE

### Objective

This git repository provides a simple PySpark Unit Testing example in Cloudera Data Engineering (CDE). With CDE, you can streamline your Spark Unit Tests with CDE Spark Jobs and Files Resources. Leveraging these two CDE features you can build modular and reusable tests. In addition, CDE provides extensive Job Monitoring and Observability features so you can trace every Unit Test run with its associated dependencies.

### Brief Introduction to CDE

CDE is the only cloud-native service purpose-built for enterprise data engineering teams. Building on Apache Spark, Data Engineering is an all-inclusive data engineering toolset that enables orchestration automation with Apache Airflow, advanced pipeline monitoring, visual troubleshooting, and comprehensive management tools to streamline ETL processes across enterprise analytics teams.

CDE is fully integrated with Cloudera Data Platform (CDP), enabling end-to-end visibility and security with SDX as well as seamless integrations with CDP services such as Data Warehouse and Machine Learning. Data Engineering on CDP powers consistent, repeatable, and automated data engineering workflows on a hybrid cloud platform anywhere.

For more information on Cloudera Data Engineering please visit the [official documentation](https://docs.cloudera.com/data-engineering/cloud/index.html).

### Requirements

The following are required to reproduce this example in your CDE Virtual Cluster:

* CDE Service version 1.17 or above with Spark version 2.4 or above.
* A Working installation of the CDE CLI. Instructions to install the CLI are provided [here](https://docs.cloudera.com/data-engineering/cloud/cli-access/topics/cde-cli.html).
* A working installation of git in your local machine. Please clone this git repository and keep in mind all commands assume they are run in the project's main directory.
* No code edits required but familiarity with [Python](https://www.python.org/), [Spark](https://spark.apache.org/) and the [unittest framework](https://docs.python.org/3/library/unittest.html) is recommended.

### Step by Step Instructions

##### 1. Create CDE Files Resource

```
cde resource create --name my_unit_testing_files \
                    --type files
```

##### 2. Upload files to CDE Files Resource

```
cde resource upload --name my_unit_testing_files \
                    --local-path data/my_data.csv \
                    --local-path main.py \
                    --local-path my_transformations.py \
                    --local-path unit_tests.py
```

##### 3. Create and Run CDE Spark Job for Spark Application

Create the CDE Job of Type Spark for the Main Application.
Use the "main.py" script as the Spark Application file.
Mount files in the my_unit_testing_files CDE Resource of type Files.

```
cde job create --name my_spark_application \
                --type spark \
                --application-file main.py \
                --mount-1-resource my_unit_testing_files
```

Run the CDE Job with the Main Application code.
Pass the data file path as an argument.

```
cde job run --name my_spark_application \
                    --arg "/app/mount/my_data.csv"
```

##### 4. Create and Run CDE Spark Job for Unit Test

Create the CDE Job of Type Spark for the Unit Testing Application.
Use the "unit_tests.py" script as the Spark Application file.
Mount files in the my_unit_testing_files CDE Resource of type Files.

```
cde job create --name my_unit_tests \
                    --application-file unit_tests.py \
                    --mount-N-resource my_unit_testing_files
```

Run the CDE Job with the Unit Tests.

```
cde job run --name my_unit_tests
```

##### 5. Monitor outputs in the CDE Job Runs page.

Navigate to the Job Runs page in your CDE Virtual Cluster. Open the "stdout" logs and validate unit test outputs.

### Summary

In this example we have run two simple PySpark Unit Tests in CDE. Here are the key takeaways from this exercise:

* Unlike raw Spark-Submits in a Spark Cluster, CDE Job Definitions are clear and reusable. This means you can better organize your unit tests into CDE Spark Job Abstractions.
* Unlike in a Spark Cluster, CDE provides Files Resources to upload Spark Job dependencies. Just like CDE Job Definitions, CDE Files Resources are also reusable. When you build your Unit Test Cases you can more easily reference files and dependencies.
* CDE provides built-in Observability. By simply visiting the Job Runs UI (or using the CLI and API) you can monitor unit test outcomes in a clear and coincise manner.

### References

[Cloudera Data Engineering Documentation](https://docs.cloudera.com/data-engineering/cloud/index.html)

[Creating and Managing CDE Jobs](https://docs.cloudera.com/data-engineering/cloud/manage-jobs/topics/cde-create-job.html)

[Using CDE Resources](https://docs.cloudera.com/data-engineering/cloud/use-resources/topics/cde-python-virtual-env.html)

[Python unittest framework](https://docs.python.org/3/library/unittest.html)

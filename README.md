[![Maven Central](https://img.shields.io/maven-central/v/com.boozallen.aissemble/booz-allen-maven-licenses.svg)](https://search.maven.org/#search%7Cgav%7C1%7Cg%3A%22com.boozallen.aissemble%22%20AND%20a%3A%22booz-allen-maven-licenses%22)
[![Build](https://github.com/boozallen/booz-allen-maven-licenses/actions/workflows/build.yaml/badge.svg)](https://github.com/boozallen/booz-allen-maven-licenses/actions/workflows/build.yaml)

# license-maven-plugin

This project eases the specification and handling of Booz Allen IP rights within codebases. It serves two primary
functions:

* Adding a copyright and license file into a project
* Added header content with copyright and license info into appropriate files

It does this by providing a custom configuration Maven extension for the various Booz Allen specific license varieties
that work with the standard
MojoHaus license-maven-plugin that is commonly used throughout industry:

* Booz Allen Public License (BAPL) - allows government, non-profit academic, other non-profit, and commercial entities
  access to distinctive,
  disruptive, and robust code with the goal of Empowering People to Change the World℠; products licensed under the Booz
  Allen Public License are
  founded on the basis that collective ingenuity can make the largest impact in the community
* Booz Allen Closed Source License - all rights are restricted
* Booz Allen Government Use Rights - can be used by the Government in the execution of a specific contract
* Booz Allen Limited Government Use Rights - can be used by a specific organization within the Government for the
  execution of a specific contract

## Usage

The following options cover the core use case,
but [substantially more options exist within the MojoHaus licence-maven-plugin](https://www.mojohaus.org/license-maven-plugin/)
as well. Please see their documentation for additional details on license reporting and more.

### Common Setup

It is recommended that you leverage Maven POM extension to ease your configuration as well as improve consistency. The
following block can be added to Maven
to provide basic setup:

```xml
...
<build>
    <pluginManagement>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>license-maven-plugin</artifactId>
                <version>2.4.0</version>
                <configuration>
                    <!--TODO: Add your license choice here - more details on each option below: -->
                    <licenseName>NAME OF LICENSE HERE</licenseName>
                    <licenseResolver>classpath://com/boozallen</licenseResolver>
                </configuration>
                <executions>
                    <!-- Include this execution if you want header support: -->
                    <execution>
                        <id>update-file-header</id>
                        <goals>
                            <goal>update-file-header</goal>
                        </goals>
                        <phase>process-sources</phase>
                        <configuration>
                            <canUpdateCopyright>true</canUpdateCopyright>
                            <ignoreLastDate>true</ignoreLastDate>
                        </configuration>
                    </execution>
                    <!-- Include this execution if you want project license file support: -->
                    <execution>
                        <id>update-project-license</id>
                        <goals>
                            <goal>update-project-license</goal>
                        </goals>
                        <configuration>
                            <force>true</force>
                        </configuration>
                    </execution>
                </executions>
                <dependencies>
                    <dependency>
                        <groupId>com.boozallen.aissemble</groupId>
                        <artifactId>booz-allen-licenses</artifactId>
                        <version>${project.version}</version>
                    </dependency>
                </dependencies>
            </plugin>
        </plugins>
    </pluginManagement>
</build>
...
```

Once the above block has been added to your root pom, you can use the following setup to support specific modules.

### Specifying the Appropriate License

The following options provides configuration details for each license type.

#### Booz Allen Public License (BAPL)

Simply specify the following license name:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>license-maven-plugin</artifactId>
    ...
    <configuration>
        <licenseName>booz-allen-public-license</licenseName>
        ...
    </configuration>
</plugin>
```

#### Booz Allen Closed Source

Simply specify the following license name:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>license-maven-plugin</artifactId>
    ...
    <configuration>
        <licenseName>closed-source-license</licenseName>
        ...
    </configuration>
</plugin>
```

#### Booz Allen Government Use

Simply specify the following license name and associated parameters that will be substituted into the license
dynamically:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>license-maven-plugin</artifactId>
    ...
    <configuration>
        <licenseName>government-client-use-license</licenseName>
        <extraTemplateParameters>
            <contractNumber>YOUR CONTRACT NUMBER</contractNumber>
            <licenseNumber>LICENSE NUMBER GRANTED BY LEGAL DEPARTMENT</licenseNumber>
        </extraTemplateParameters>
        ...
    </configuration>
</plugin>
```

#### Booz Allen Limited Government Use

Simply specify the following license name and associated parameters that will be substituted into the license
dynamically

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>license-maven-plugin</artifactId>
    ...
    <configuration>
        <licenseName>limited-government-client-use-license</licenseName>
        <extraTemplateParameters>
            <contractNumber>YOUR CONTRACT NUMBER</contractNumber>
            <licenseNumber>LICENSE NUMBER GRANTED BY LEGAL DEPARTMENT</licenseNumber>
        </extraTemplateParameters>

        <!-- 
          Assuming your organization in your root pom.xml file is not Booz Allen, 
          you won't need to specify this. For this test case, it is Booz Allen, 
          so we are overriding here: 
      -->
        <organizationName>CLIENT ORGANIZATION NAME</organizationName>
    </configuration>
</plugin>
```

### Activating for Specific Modules

#### Python Projects

This assumes the use of [Habushu](https://github.com/technologybrewery/habushu).

Add the following snippet into each module that your want covered:

```xml
<build>
    ...
    <plugins>
        ...
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>license-maven-plugin</artifactId>
            <configuration>
                <!-- Customizes the default LICENSE file path and name for Python standards: -->
                <licenseFile>LICENSE</licenseFile>
            </configuration>
        </plugin>
    </plugins>
</build>
```

#### Java Projects

Add the following snippet into each module that your want covered:

```xml
<build>
    ...
    <plugins>
        ...
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>license-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```
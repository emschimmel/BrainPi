name := "StatisticPi"

version := "0.1"

scalaVersion := "2.12.4"

lazy val akkaVersion = "2.4.17"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor" % akkaVersion,
  "com.typesafe.akka" %% "akka-testkit" % akkaVersion,
  "org.scalatest" %% "scalatest" % "3.0.1" % "test",
  "com.lightbend.akka.discovery" %% "akka-discovery-dns" % "0.10.0"
//  ,
//  "com.orbitz.consul:consul-client:1.0.1"
)

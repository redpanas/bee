# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name = "bee-holy-scripture"
  spec.version = "1.0.0"
  spec.authors = ["Panagiotis Kouzaris"]
  spec.summary = "The holy scripture downloader"
  spec.description = "Downloads a pinned Bee Movie dialogue transcript and converts work-related words to leetspeak."
  spec.homepage = "https://github.com/redpanas/bee"
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"

  spec.metadata = {
    "bug_tracker_uri" => "https://github.com/redpanas/bee/issues",
    "source_code_uri" => "https://github.com/redpanas/bee"
  }

  spec.files = ["exe/bee", "README.md", "LICENSE"]
  spec.bindir = "exe"
  spec.executables = ["bee"]
end

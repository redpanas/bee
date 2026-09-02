use regex::{Captures, RegexBuilder};
use std::env;
use std::error::Error;
use std::fs;
use std::io::Write;
use std::path::{Path, PathBuf};

const VERSION: &str = "1.0.0";
const SOURCE_URL: &str = "https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script";
const REPLACEMENTS: &[(&str, &str)] = &[
    ("employees", "3mp10y33s"),
    ("employment", "3mp10ym3n7"),
    ("professional", "pr0f3$$!0n@1"),
    ("profession", "pr0f3$$!0n"),
    ("employers", "3mp10y3rs"),
    ("employer", "3mp10y3r"),
    ("employee", "3mp10y33"),
    ("employed", "3mp10y3d"),
    ("workers", "w0rk3rs"),
    ("working", "w0rk!n9"),
    ("worked", "w0rk3d"),
    ("worker", "w0rk3r"),
    ("careers", "c@r33rs"),
    ("business", "8u$!n3$$"),
    ("manager", "m@n@g3r"),
    ("salary", "$@1@ry"),
    ("career", "c@r33r"),
    ("office", "0ff!(3"),
    ("wages", "w@g3s"),
    ("staff", "$7@ff"),
    ("hired", "#!r3d"),
    ("fired", "f!r3d"),
    ("works", "w0rks"),
    ("wage", "w@g3"),
    ("hire", "#!r3"),
    ("jobs", "j08s"),
    ("work", "w0rk"),
    ("boss", "80$$"),
    ("job", "j08"),
];

fn usage() {
    println!("Usage: bee [OUTPUT_FILE]\n\nDownload and publish the holy scripture.");
}

fn transform(mut text: String) -> Result<String, regex::Error> {
    for (word, replacement) in REPLACEMENTS {
        let expression = RegexBuilder::new(&format!(r"\b{}\b", regex::escape(word)))
            .case_insensitive(true)
            .build()?;
        text = expression
            .replace_all(&text, |_: &Captures<'_>| *replacement)
            .into_owned();
    }
    Ok(text)
}

fn publish(output: &Path) -> Result<(), Box<dyn Error>> {
    let response = ureq::get(SOURCE_URL).call()?;
    let scripture = transform(response.into_string()?)?;
    let directory = output.parent().unwrap_or_else(|| Path::new("."));
    let mut temporary = tempfile::NamedTempFile::new_in(directory)?;
    temporary.write_all(scripture.as_bytes())?;
    temporary.flush()?;

    if output.exists() {
        fs::remove_file(output)?;
    }
    temporary.persist(output)?;
    Ok(())
}

fn main() {
    let args: Vec<_> = env::args_os().skip(1).collect();
    let first = args.first().map(|arg| arg.to_string_lossy());

    match first.as_deref() {
        Some("-h" | "--help") => {
            usage();
            return;
        }
        Some("-v" | "--version") => {
            println!("bee {VERSION}");
            return;
        }
        Some(option) if option.starts_with('-') => {
            eprintln!("bee: unknown option: {option}");
            std::process::exit(2);
        }
        _ => {}
    }

    if args.len() > 1 {
        usage();
        std::process::exit(2);
    }

    let output = args
        .first()
        .map(PathBuf::from)
        .unwrap_or_else(|| PathBuf::from("the_holy_scripture.txt"));
    if let Err(error) = publish(&output) {
        eprintln!("bee: {error}");
        std::process::exit(1);
    }
    println!("Published the holy scripture to {}", output.display());
}

#[cfg(test)]
mod tests {
    use super::transform;

    #[test]
    fn transforms_case_insensitive_whole_words() {
        assert_eq!(
            transform("Job WORK workers.".into()).unwrap(),
            "j08 w0rk w0rk3rs."
        );
    }
}
